# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.swap_cashout_result import SwapCashoutResult
import re
from openapi_server import util

from openapi_server.models.swap_cashout_result import SwapCashoutResult  # noqa: E501
import re  # noqa: E501

class SwapCashoutStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, peer=None, chequebook=None, cumulative_payout=None, beneficiary=None, transaction_hash=None, result=None):  # noqa: E501
        """SwapCashoutStatus - a model defined in OpenAPI

        :param peer: The peer of this SwapCashoutStatus.  # noqa: E501
        :type peer: str
        :param chequebook: The chequebook of this SwapCashoutStatus.  # noqa: E501
        :type chequebook: str
        :param cumulative_payout: The cumulative_payout of this SwapCashoutStatus.  # noqa: E501
        :type cumulative_payout: int
        :param beneficiary: The beneficiary of this SwapCashoutStatus.  # noqa: E501
        :type beneficiary: str
        :param transaction_hash: The transaction_hash of this SwapCashoutStatus.  # noqa: E501
        :type transaction_hash: str
        :param result: The result of this SwapCashoutStatus.  # noqa: E501
        :type result: SwapCashoutResult
        """
        self.openapi_types = {
            'peer': str,
            'chequebook': str,
            'cumulative_payout': int,
            'beneficiary': str,
            'transaction_hash': str,
            'result': SwapCashoutResult
        }

        self.attribute_map = {
            'peer': 'peer',
            'chequebook': 'chequebook',
            'cumulative_payout': 'cumulativePayout',
            'beneficiary': 'beneficiary',
            'transaction_hash': 'transactionHash',
            'result': 'result'
        }

        self._peer = peer
        self._chequebook = chequebook
        self._cumulative_payout = cumulative_payout
        self._beneficiary = beneficiary
        self._transaction_hash = transaction_hash
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'SwapCashoutStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SwapCashoutStatus of this SwapCashoutStatus.  # noqa: E501
        :rtype: SwapCashoutStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def peer(self):
        """Gets the peer of this SwapCashoutStatus.


        :return: The peer of this SwapCashoutStatus.
        :rtype: str
        """
        return self._peer

    @peer.setter
    def peer(self, peer):
        """Sets the peer of this SwapCashoutStatus.


        :param peer: The peer of this SwapCashoutStatus.
        :type peer: str
        """
        if peer is not None and not re.search(r'^[A-Fa-f0-9]{64}$', peer):  # noqa: E501
            raise ValueError("Invalid value for `peer`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{64}$/`")  # noqa: E501

        self._peer = peer

    @property
    def chequebook(self):
        """Gets the chequebook of this SwapCashoutStatus.


        :return: The chequebook of this SwapCashoutStatus.
        :rtype: str
        """
        return self._chequebook

    @chequebook.setter
    def chequebook(self, chequebook):
        """Sets the chequebook of this SwapCashoutStatus.


        :param chequebook: The chequebook of this SwapCashoutStatus.
        :type chequebook: str
        """
        if chequebook is not None and not re.search(r'^[A-Fa-f0-9]{40}$', chequebook):  # noqa: E501
            raise ValueError("Invalid value for `chequebook`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{40}$/`")  # noqa: E501

        self._chequebook = chequebook

    @property
    def cumulative_payout(self):
        """Gets the cumulative_payout of this SwapCashoutStatus.


        :return: The cumulative_payout of this SwapCashoutStatus.
        :rtype: int
        """
        return self._cumulative_payout

    @cumulative_payout.setter
    def cumulative_payout(self, cumulative_payout):
        """Sets the cumulative_payout of this SwapCashoutStatus.


        :param cumulative_payout: The cumulative_payout of this SwapCashoutStatus.
        :type cumulative_payout: int
        """

        self._cumulative_payout = cumulative_payout

    @property
    def beneficiary(self):
        """Gets the beneficiary of this SwapCashoutStatus.


        :return: The beneficiary of this SwapCashoutStatus.
        :rtype: str
        """
        return self._beneficiary

    @beneficiary.setter
    def beneficiary(self, beneficiary):
        """Sets the beneficiary of this SwapCashoutStatus.


        :param beneficiary: The beneficiary of this SwapCashoutStatus.
        :type beneficiary: str
        """
        if beneficiary is not None and not re.search(r'^[A-Fa-f0-9]{40}$', beneficiary):  # noqa: E501
            raise ValueError("Invalid value for `beneficiary`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{40}$/`")  # noqa: E501

        self._beneficiary = beneficiary

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this SwapCashoutStatus.


        :return: The transaction_hash of this SwapCashoutStatus.
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this SwapCashoutStatus.


        :param transaction_hash: The transaction_hash of this SwapCashoutStatus.
        :type transaction_hash: str
        """
        if transaction_hash is not None and not re.search(r'^[A-Fa-f0-9]{64}$', transaction_hash):  # noqa: E501
            raise ValueError("Invalid value for `transaction_hash`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{64}$/`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def result(self):
        """Gets the result of this SwapCashoutStatus.


        :return: The result of this SwapCashoutStatus.
        :rtype: SwapCashoutResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SwapCashoutStatus.


        :param result: The result of this SwapCashoutStatus.
        :type result: SwapCashoutResult
        """

        self._result = result