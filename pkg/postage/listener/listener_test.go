package listener_test

import (
	"context"
	"encoding/hex"
	"fmt"
	"math/big"
	"strings"
	"testing"
	"time"

	"github.com/ethereum/go-ethereum"
	"github.com/ethereum/go-ethereum/accounts/abi"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethersphere/bee/pkg/crypto"
	"github.com/ethersphere/bee/pkg/postage/listener"
)

var hash common.Hash
var addr common.Address
var createdTopic = common.HexToHash("3f6ec1ed9250a6952fabac07c6eb103550dc65175373eea432fd115ce8bb2246")

func init() {
	a := make([]byte, 20)
	a[0] = 20
	copy(addr[:], a)
	h := make([]byte, 32)
	copy(hash[:], h)
}

func TestListener(t *testing.T) {
	// test that when the listener gets a certain event
	// then we would like to assert the appropriate EventUpdater method was called
	//mockId := make([]byte, 32)
	//mockOwner := make([]byte, 32)
	ev := newEventUpdaterMock()
	mf := newMockFilterer(newCreateEvent())
	listener := listener.New(mf)
	listener.Listen(0, ev)
	for i := 0; i < 10; i++ {
		if ev.createCalled {
			return
			t.Log("expected Create event to be called")
		}
		time.Sleep(100 * time.Millisecond)
	}
	t.Fatal("timed out")
}

func newEventUpdaterMock() *updater {
	return &updater{}
}

type updater struct {
	createCalled      bool
	topupCalled       bool
	updateDepthCalled bool
	updatePriceCalled bool
}

func (u *updater) Create(id []byte, owner []byte, amount *big.Int, depth uint8) error {
	fmt.Println(id)
	fmt.Println(owner)
	fmt.Println(depth)
	fmt.Println(amount)
	u.createCalled = true
	return nil
}

func (u *updater) TopUp(id []byte, amount *big.Int) error {
	u.topupCalled = true
	return nil
}

func (u *updater) UpdateDepth(id []byte, depth uint8) error {
	u.updateDepthCalled = true
	return nil
}

func (u *updater) UpdatePrice(price *big.Int) error {
	u.updatePriceCalled = true
	return nil
}

type mockFilterer struct {
	events []types.Log
	sub    *sub
}

func newMockFilterer(logs ...types.Log) *mockFilterer {
	return &mockFilterer{
		events: logs,
	}
}

func (m *mockFilterer) FilterLogs(ctx context.Context, query ethereum.FilterQuery) ([]types.Log, error) {
	return m.events, nil
}

func (m *mockFilterer) SubscribeFilterLogs(ctx context.Context, query ethereum.FilterQuery, ch chan<- types.Log) (ethereum.Subscription, error) {
	go func() {
		for _, ev := range m.events {
			ch <- ev
		}
	}()
	s := newSub()
	return s, nil
}

func (m *mockFilterer) Close() {
	close(m.sub.c)
}

func (m *mockFilterer) BlockHeight(context.Context) (uint64, error) {
	return 0, nil
}

func parseABI(json string) abi.ABI {
	cabi, err := abi.JSON(strings.NewReader(json))
	if err != nil {
		panic(fmt.Sprintf("error creating ABI for postage contract: %v", err))
	}
	return cabi
}

func newCreateEvent() types.Log {
	a := parseABI(listener.Abi)
	b, err := a.Events["BatchCreated"].Inputs.Pack(hash, big.NewInt(42), big.NewInt(42), addr, uint8(12))
	if err != nil {
		panic(err)
	}
	fmt.Println(b)
	l := types.Log{
		Data:   b,
		Topics: []common.Hash{createdTopic, hash}, // 1st item is the function sig digest, 2nd is always the batch id
	}

	return l

}

type sub struct {
	c chan error
}

func newSub() *sub {
	return &sub{
		c: make(chan error),
	}
}

func (s *sub) Unsubscribe() {}
func (s *sub) Err() <-chan error {
	return s.c
}

func TestT(t *testing.T) {
	eventSignatures := []string{
		"BatchCreated(bytes32,uint256,uint256,address,uint8)",
		"BatchTopUp(bytes32,uint256)",
		"BatchDepthIncrease(bytes32,uint256)",
		"PriceUpdate(uint256)",
	}

	t.Fatal(digestSig(eventSignatures))
}

func digestSig(sigs []string) []string {
	digests := make([]string, 4)
	for i, s := range sigs {
		h, err := crypto.LegacyKeccak256([]byte(s))
		if err != nil {
			panic(fmt.Sprintf("error digesting signatures: %v", err))
		}
		digests[i] = hex.EncodeToString(h)
	}
	return digests
}