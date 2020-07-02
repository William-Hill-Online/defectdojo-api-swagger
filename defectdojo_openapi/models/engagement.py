# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from defectdojo_openapi.configuration import Configuration


class Engagement(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'tags': 'list[str]',
        'name': 'str',
        'description': 'str',
        'version': 'str',
        'first_contacted': 'date',
        'target_start': 'date',
        'target_end': 'date',
        'reason': 'str',
        'updated': 'datetime',
        'created': 'datetime',
        'active': 'bool',
        'tracker': 'str',
        'test_strategy': 'str',
        'threat_model': 'bool',
        'api_test': 'bool',
        'pen_test': 'bool',
        'check_list': 'bool',
        'status': 'str',
        'progress': 'str',
        'tmodel_path': 'str',
        'risk_path': 'str',
        'done_testing': 'bool',
        'engagement_type': 'str',
        'build_id': 'str',
        'commit_hash': 'str',
        'branch_tag': 'str',
        'source_code_management_uri': 'str',
        'deduplication_on_engagement': 'bool',
        'eng_type': 'int',
        'lead': 'int',
        'requester': 'int',
        'preset': 'int',
        'report_type': 'int',
        'product': 'int',
        'build_server': 'int',
        'source_code_management_server': 'int',
        'orchestration_engine': 'int',
        'risk_acceptance': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'tags': 'tags',
        'name': 'name',
        'description': 'description',
        'version': 'version',
        'first_contacted': 'first_contacted',
        'target_start': 'target_start',
        'target_end': 'target_end',
        'reason': 'reason',
        'updated': 'updated',
        'created': 'created',
        'active': 'active',
        'tracker': 'tracker',
        'test_strategy': 'test_strategy',
        'threat_model': 'threat_model',
        'api_test': 'api_test',
        'pen_test': 'pen_test',
        'check_list': 'check_list',
        'status': 'status',
        'progress': 'progress',
        'tmodel_path': 'tmodel_path',
        'risk_path': 'risk_path',
        'done_testing': 'done_testing',
        'engagement_type': 'engagement_type',
        'build_id': 'build_id',
        'commit_hash': 'commit_hash',
        'branch_tag': 'branch_tag',
        'source_code_management_uri': 'source_code_management_uri',
        'deduplication_on_engagement': 'deduplication_on_engagement',
        'eng_type': 'eng_type',
        'lead': 'lead',
        'requester': 'requester',
        'preset': 'preset',
        'report_type': 'report_type',
        'product': 'product',
        'build_server': 'build_server',
        'source_code_management_server': 'source_code_management_server',
        'orchestration_engine': 'orchestration_engine',
        'risk_acceptance': 'risk_acceptance'
    }

    def __init__(self, id=None, tags=None, name=None, description=None, version=None, first_contacted=None, target_start=None, target_end=None, reason=None, updated=None, created=None, active=None, tracker=None, test_strategy=None, threat_model=None, api_test=None, pen_test=None, check_list=None, status=None, progress=None, tmodel_path=None, risk_path=None, done_testing=None, engagement_type=None, build_id=None, commit_hash=None, branch_tag=None, source_code_management_uri=None, deduplication_on_engagement=None, eng_type=None, lead=None, requester=None, preset=None, report_type=None, product=None, build_server=None, source_code_management_server=None, orchestration_engine=None, risk_acceptance=None, local_vars_configuration=None):  # noqa: E501
        """Engagement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._tags = None
        self._name = None
        self._description = None
        self._version = None
        self._first_contacted = None
        self._target_start = None
        self._target_end = None
        self._reason = None
        self._updated = None
        self._created = None
        self._active = None
        self._tracker = None
        self._test_strategy = None
        self._threat_model = None
        self._api_test = None
        self._pen_test = None
        self._check_list = None
        self._status = None
        self._progress = None
        self._tmodel_path = None
        self._risk_path = None
        self._done_testing = None
        self._engagement_type = None
        self._build_id = None
        self._commit_hash = None
        self._branch_tag = None
        self._source_code_management_uri = None
        self._deduplication_on_engagement = None
        self._eng_type = None
        self._lead = None
        self._requester = None
        self._preset = None
        self._report_type = None
        self._product = None
        self._build_server = None
        self._source_code_management_server = None
        self._orchestration_engine = None
        self._risk_acceptance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tags is not None:
            self.tags = tags
        self.name = name
        self.description = description
        self.version = version
        self.first_contacted = first_contacted
        self.target_start = target_start
        self.target_end = target_end
        self.reason = reason
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if active is not None:
            self.active = active
        self.tracker = tracker
        self.test_strategy = test_strategy
        if threat_model is not None:
            self.threat_model = threat_model
        if api_test is not None:
            self.api_test = api_test
        if pen_test is not None:
            self.pen_test = pen_test
        if check_list is not None:
            self.check_list = check_list
        self.status = status
        if progress is not None:
            self.progress = progress
        if tmodel_path is not None:
            self.tmodel_path = tmodel_path
        if risk_path is not None:
            self.risk_path = risk_path
        if done_testing is not None:
            self.done_testing = done_testing
        self.engagement_type = engagement_type
        self.build_id = build_id
        self.commit_hash = commit_hash
        self.branch_tag = branch_tag
        self.source_code_management_uri = source_code_management_uri
        if deduplication_on_engagement is not None:
            self.deduplication_on_engagement = deduplication_on_engagement
        self.eng_type = eng_type
        self.lead = lead
        self.requester = requester
        self.preset = preset
        self.report_type = report_type
        self.product = product
        self.build_server = build_server
        self.source_code_management_server = source_code_management_server
        self.orchestration_engine = orchestration_engine
        if risk_acceptance is not None:
            self.risk_acceptance = risk_acceptance

    @property
    def id(self):
        """Gets the id of this Engagement.  # noqa: E501


        :return: The id of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Engagement.


        :param id: The id of this Engagement.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def tags(self):
        """Gets the tags of this Engagement.  # noqa: E501


        :return: The tags of this Engagement.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Engagement.


        :param tags: The tags of this Engagement.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def name(self):
        """Gets the name of this Engagement.  # noqa: E501


        :return: The name of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Engagement.


        :param name: The name of this Engagement.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 300):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `300`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Engagement.  # noqa: E501


        :return: The description of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Engagement.


        :param description: The description of this Engagement.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 2000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `2000`")  # noqa: E501

        self._description = description

    @property
    def version(self):
        """Gets the version of this Engagement.  # noqa: E501

        Version of the product the engagement tested.  # noqa: E501

        :return: The version of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Engagement.

        Version of the product the engagement tested.  # noqa: E501

        :param version: The version of this Engagement.  # noqa: E501
        :type version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 100):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `100`")  # noqa: E501

        self._version = version

    @property
    def first_contacted(self):
        """Gets the first_contacted of this Engagement.  # noqa: E501


        :return: The first_contacted of this Engagement.  # noqa: E501
        :rtype: date
        """
        return self._first_contacted

    @first_contacted.setter
    def first_contacted(self, first_contacted):
        """Sets the first_contacted of this Engagement.


        :param first_contacted: The first_contacted of this Engagement.  # noqa: E501
        :type first_contacted: date
        """

        self._first_contacted = first_contacted

    @property
    def target_start(self):
        """Gets the target_start of this Engagement.  # noqa: E501


        :return: The target_start of this Engagement.  # noqa: E501
        :rtype: date
        """
        return self._target_start

    @target_start.setter
    def target_start(self, target_start):
        """Sets the target_start of this Engagement.


        :param target_start: The target_start of this Engagement.  # noqa: E501
        :type target_start: date
        """
        if self.local_vars_configuration.client_side_validation and target_start is None:  # noqa: E501
            raise ValueError("Invalid value for `target_start`, must not be `None`")  # noqa: E501

        self._target_start = target_start

    @property
    def target_end(self):
        """Gets the target_end of this Engagement.  # noqa: E501


        :return: The target_end of this Engagement.  # noqa: E501
        :rtype: date
        """
        return self._target_end

    @target_end.setter
    def target_end(self, target_end):
        """Sets the target_end of this Engagement.


        :param target_end: The target_end of this Engagement.  # noqa: E501
        :type target_end: date
        """
        if self.local_vars_configuration.client_side_validation and target_end is None:  # noqa: E501
            raise ValueError("Invalid value for `target_end`, must not be `None`")  # noqa: E501

        self._target_end = target_end

    @property
    def reason(self):
        """Gets the reason of this Engagement.  # noqa: E501


        :return: The reason of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Engagement.


        :param reason: The reason of this Engagement.  # noqa: E501
        :type reason: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reason is not None and len(reason) > 2000):
            raise ValueError("Invalid value for `reason`, length must be less than or equal to `2000`")  # noqa: E501

        self._reason = reason

    @property
    def updated(self):
        """Gets the updated of this Engagement.  # noqa: E501


        :return: The updated of this Engagement.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Engagement.


        :param updated: The updated of this Engagement.  # noqa: E501
        :type updated: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this Engagement.  # noqa: E501


        :return: The created of this Engagement.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Engagement.


        :param created: The created of this Engagement.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def active(self):
        """Gets the active of this Engagement.  # noqa: E501


        :return: The active of this Engagement.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Engagement.


        :param active: The active of this Engagement.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def tracker(self):
        """Gets the tracker of this Engagement.  # noqa: E501

        Link to epic or ticket system with changes to version.  # noqa: E501

        :return: The tracker of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        """Sets the tracker of this Engagement.

        Link to epic or ticket system with changes to version.  # noqa: E501

        :param tracker: The tracker of this Engagement.  # noqa: E501
        :type tracker: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tracker is not None and len(tracker) > 200):
            raise ValueError("Invalid value for `tracker`, length must be less than or equal to `200`")  # noqa: E501

        self._tracker = tracker

    @property
    def test_strategy(self):
        """Gets the test_strategy of this Engagement.  # noqa: E501


        :return: The test_strategy of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._test_strategy

    @test_strategy.setter
    def test_strategy(self, test_strategy):
        """Sets the test_strategy of this Engagement.


        :param test_strategy: The test_strategy of this Engagement.  # noqa: E501
        :type test_strategy: str
        """
        if (self.local_vars_configuration.client_side_validation and
                test_strategy is not None and len(test_strategy) > 200):
            raise ValueError("Invalid value for `test_strategy`, length must be less than or equal to `200`")  # noqa: E501

        self._test_strategy = test_strategy

    @property
    def threat_model(self):
        """Gets the threat_model of this Engagement.  # noqa: E501


        :return: The threat_model of this Engagement.  # noqa: E501
        :rtype: bool
        """
        return self._threat_model

    @threat_model.setter
    def threat_model(self, threat_model):
        """Sets the threat_model of this Engagement.


        :param threat_model: The threat_model of this Engagement.  # noqa: E501
        :type threat_model: bool
        """

        self._threat_model = threat_model

    @property
    def api_test(self):
        """Gets the api_test of this Engagement.  # noqa: E501


        :return: The api_test of this Engagement.  # noqa: E501
        :rtype: bool
        """
        return self._api_test

    @api_test.setter
    def api_test(self, api_test):
        """Sets the api_test of this Engagement.


        :param api_test: The api_test of this Engagement.  # noqa: E501
        :type api_test: bool
        """

        self._api_test = api_test

    @property
    def pen_test(self):
        """Gets the pen_test of this Engagement.  # noqa: E501


        :return: The pen_test of this Engagement.  # noqa: E501
        :rtype: bool
        """
        return self._pen_test

    @pen_test.setter
    def pen_test(self, pen_test):
        """Sets the pen_test of this Engagement.


        :param pen_test: The pen_test of this Engagement.  # noqa: E501
        :type pen_test: bool
        """

        self._pen_test = pen_test

    @property
    def check_list(self):
        """Gets the check_list of this Engagement.  # noqa: E501


        :return: The check_list of this Engagement.  # noqa: E501
        :rtype: bool
        """
        return self._check_list

    @check_list.setter
    def check_list(self, check_list):
        """Sets the check_list of this Engagement.


        :param check_list: The check_list of this Engagement.  # noqa: E501
        :type check_list: bool
        """

        self._check_list = check_list

    @property
    def status(self):
        """Gets the status of this Engagement.  # noqa: E501


        :return: The status of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Engagement.


        :param status: The status of this Engagement.  # noqa: E501
        :type status: str
        """
        allowed_values = [None,"Not Started", "Blocked", "Cancelled", "Completed", "In Progress", "On Hold", "Waiting for Resource"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this Engagement.  # noqa: E501


        :return: The progress of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Engagement.


        :param progress: The progress of this Engagement.  # noqa: E501
        :type progress: str
        """
        if (self.local_vars_configuration.client_side_validation and
                progress is not None and len(progress) < 1):
            raise ValueError("Invalid value for `progress`, length must be greater than or equal to `1`")  # noqa: E501

        self._progress = progress

    @property
    def tmodel_path(self):
        """Gets the tmodel_path of this Engagement.  # noqa: E501


        :return: The tmodel_path of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._tmodel_path

    @tmodel_path.setter
    def tmodel_path(self, tmodel_path):
        """Sets the tmodel_path of this Engagement.


        :param tmodel_path: The tmodel_path of this Engagement.  # noqa: E501
        :type tmodel_path: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tmodel_path is not None and len(tmodel_path) < 1):
            raise ValueError("Invalid value for `tmodel_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._tmodel_path = tmodel_path

    @property
    def risk_path(self):
        """Gets the risk_path of this Engagement.  # noqa: E501


        :return: The risk_path of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._risk_path

    @risk_path.setter
    def risk_path(self, risk_path):
        """Sets the risk_path of this Engagement.


        :param risk_path: The risk_path of this Engagement.  # noqa: E501
        :type risk_path: str
        """
        if (self.local_vars_configuration.client_side_validation and
                risk_path is not None and len(risk_path) < 1):
            raise ValueError("Invalid value for `risk_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._risk_path = risk_path

    @property
    def done_testing(self):
        """Gets the done_testing of this Engagement.  # noqa: E501


        :return: The done_testing of this Engagement.  # noqa: E501
        :rtype: bool
        """
        return self._done_testing

    @done_testing.setter
    def done_testing(self, done_testing):
        """Sets the done_testing of this Engagement.


        :param done_testing: The done_testing of this Engagement.  # noqa: E501
        :type done_testing: bool
        """

        self._done_testing = done_testing

    @property
    def engagement_type(self):
        """Gets the engagement_type of this Engagement.  # noqa: E501


        :return: The engagement_type of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._engagement_type

    @engagement_type.setter
    def engagement_type(self, engagement_type):
        """Sets the engagement_type of this Engagement.


        :param engagement_type: The engagement_type of this Engagement.  # noqa: E501
        :type engagement_type: str
        """
        allowed_values = [None,"Interactive", "CI/CD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and engagement_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `engagement_type` ({0}), must be one of {1}"  # noqa: E501
                .format(engagement_type, allowed_values)
            )

        self._engagement_type = engagement_type

    @property
    def build_id(self):
        """Gets the build_id of this Engagement.  # noqa: E501

        Build ID of the product the engagement tested.  # noqa: E501

        :return: The build_id of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this Engagement.

        Build ID of the product the engagement tested.  # noqa: E501

        :param build_id: The build_id of this Engagement.  # noqa: E501
        :type build_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                build_id is not None and len(build_id) > 150):
            raise ValueError("Invalid value for `build_id`, length must be less than or equal to `150`")  # noqa: E501

        self._build_id = build_id

    @property
    def commit_hash(self):
        """Gets the commit_hash of this Engagement.  # noqa: E501

        Commit hash from repo  # noqa: E501

        :return: The commit_hash of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this Engagement.

        Commit hash from repo  # noqa: E501

        :param commit_hash: The commit_hash of this Engagement.  # noqa: E501
        :type commit_hash: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commit_hash is not None and len(commit_hash) > 150):
            raise ValueError("Invalid value for `commit_hash`, length must be less than or equal to `150`")  # noqa: E501

        self._commit_hash = commit_hash

    @property
    def branch_tag(self):
        """Gets the branch_tag of this Engagement.  # noqa: E501

        Tag or branch of the product the engagement tested.  # noqa: E501

        :return: The branch_tag of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._branch_tag

    @branch_tag.setter
    def branch_tag(self, branch_tag):
        """Sets the branch_tag of this Engagement.

        Tag or branch of the product the engagement tested.  # noqa: E501

        :param branch_tag: The branch_tag of this Engagement.  # noqa: E501
        :type branch_tag: str
        """
        if (self.local_vars_configuration.client_side_validation and
                branch_tag is not None and len(branch_tag) > 150):
            raise ValueError("Invalid value for `branch_tag`, length must be less than or equal to `150`")  # noqa: E501

        self._branch_tag = branch_tag

    @property
    def source_code_management_uri(self):
        """Gets the source_code_management_uri of this Engagement.  # noqa: E501

        Resource link to source code  # noqa: E501

        :return: The source_code_management_uri of this Engagement.  # noqa: E501
        :rtype: str
        """
        return self._source_code_management_uri

    @source_code_management_uri.setter
    def source_code_management_uri(self, source_code_management_uri):
        """Sets the source_code_management_uri of this Engagement.

        Resource link to source code  # noqa: E501

        :param source_code_management_uri: The source_code_management_uri of this Engagement.  # noqa: E501
        :type source_code_management_uri: str
        """
        if (self.local_vars_configuration.client_side_validation and
                source_code_management_uri is not None and len(source_code_management_uri) > 600):
            raise ValueError("Invalid value for `source_code_management_uri`, length must be less than or equal to `600`")  # noqa: E501

        self._source_code_management_uri = source_code_management_uri

    @property
    def deduplication_on_engagement(self):
        """Gets the deduplication_on_engagement of this Engagement.  # noqa: E501


        :return: The deduplication_on_engagement of this Engagement.  # noqa: E501
        :rtype: bool
        """
        return self._deduplication_on_engagement

    @deduplication_on_engagement.setter
    def deduplication_on_engagement(self, deduplication_on_engagement):
        """Sets the deduplication_on_engagement of this Engagement.


        :param deduplication_on_engagement: The deduplication_on_engagement of this Engagement.  # noqa: E501
        :type deduplication_on_engagement: bool
        """

        self._deduplication_on_engagement = deduplication_on_engagement

    @property
    def eng_type(self):
        """Gets the eng_type of this Engagement.  # noqa: E501


        :return: The eng_type of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._eng_type

    @eng_type.setter
    def eng_type(self, eng_type):
        """Sets the eng_type of this Engagement.


        :param eng_type: The eng_type of this Engagement.  # noqa: E501
        :type eng_type: int
        """

        self._eng_type = eng_type

    @property
    def lead(self):
        """Gets the lead of this Engagement.  # noqa: E501


        :return: The lead of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._lead

    @lead.setter
    def lead(self, lead):
        """Sets the lead of this Engagement.


        :param lead: The lead of this Engagement.  # noqa: E501
        :type lead: int
        """

        self._lead = lead

    @property
    def requester(self):
        """Gets the requester of this Engagement.  # noqa: E501


        :return: The requester of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._requester

    @requester.setter
    def requester(self, requester):
        """Sets the requester of this Engagement.


        :param requester: The requester of this Engagement.  # noqa: E501
        :type requester: int
        """

        self._requester = requester

    @property
    def preset(self):
        """Gets the preset of this Engagement.  # noqa: E501

        Settings and notes for performing this engagement.  # noqa: E501

        :return: The preset of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this Engagement.

        Settings and notes for performing this engagement.  # noqa: E501

        :param preset: The preset of this Engagement.  # noqa: E501
        :type preset: int
        """

        self._preset = preset

    @property
    def report_type(self):
        """Gets the report_type of this Engagement.  # noqa: E501


        :return: The report_type of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this Engagement.


        :param report_type: The report_type of this Engagement.  # noqa: E501
        :type report_type: int
        """

        self._report_type = report_type

    @property
    def product(self):
        """Gets the product of this Engagement.  # noqa: E501


        :return: The product of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Engagement.


        :param product: The product of this Engagement.  # noqa: E501
        :type product: int
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def build_server(self):
        """Gets the build_server of this Engagement.  # noqa: E501

        Build server responsible for CI/CD test  # noqa: E501

        :return: The build_server of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._build_server

    @build_server.setter
    def build_server(self, build_server):
        """Sets the build_server of this Engagement.

        Build server responsible for CI/CD test  # noqa: E501

        :param build_server: The build_server of this Engagement.  # noqa: E501
        :type build_server: int
        """

        self._build_server = build_server

    @property
    def source_code_management_server(self):
        """Gets the source_code_management_server of this Engagement.  # noqa: E501

        Source code server for CI/CD test  # noqa: E501

        :return: The source_code_management_server of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._source_code_management_server

    @source_code_management_server.setter
    def source_code_management_server(self, source_code_management_server):
        """Sets the source_code_management_server of this Engagement.

        Source code server for CI/CD test  # noqa: E501

        :param source_code_management_server: The source_code_management_server of this Engagement.  # noqa: E501
        :type source_code_management_server: int
        """

        self._source_code_management_server = source_code_management_server

    @property
    def orchestration_engine(self):
        """Gets the orchestration_engine of this Engagement.  # noqa: E501

        Orchestration service responsible for CI/CD test  # noqa: E501

        :return: The orchestration_engine of this Engagement.  # noqa: E501
        :rtype: int
        """
        return self._orchestration_engine

    @orchestration_engine.setter
    def orchestration_engine(self, orchestration_engine):
        """Sets the orchestration_engine of this Engagement.

        Orchestration service responsible for CI/CD test  # noqa: E501

        :param orchestration_engine: The orchestration_engine of this Engagement.  # noqa: E501
        :type orchestration_engine: int
        """

        self._orchestration_engine = orchestration_engine

    @property
    def risk_acceptance(self):
        """Gets the risk_acceptance of this Engagement.  # noqa: E501


        :return: The risk_acceptance of this Engagement.  # noqa: E501
        :rtype: list[int]
        """
        return self._risk_acceptance

    @risk_acceptance.setter
    def risk_acceptance(self, risk_acceptance):
        """Sets the risk_acceptance of this Engagement.


        :param risk_acceptance: The risk_acceptance of this Engagement.  # noqa: E501
        :type risk_acceptance: list[int]
        """

        self._risk_acceptance = risk_acceptance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Engagement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Engagement):
            return True

        return self.to_dict() != other.to_dict()