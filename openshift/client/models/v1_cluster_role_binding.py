# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ClusterRoleBinding(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'group_names': 'list[str]',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'role_ref': 'V1ObjectReference',
        'subjects': 'list[V1ObjectReference]',
        'user_names': 'list[str]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'group_names': 'groupNames',
        'kind': 'kind',
        'metadata': 'metadata',
        'role_ref': 'roleRef',
        'subjects': 'subjects',
        'user_names': 'userNames'
    }

    def __init__(self, api_version=None, group_names=None, kind=None, metadata=None, role_ref=None, subjects=None, user_names=None):
        """
        V1ClusterRoleBinding - a model defined in Swagger
        """

        self._api_version = None
        self._group_names = None
        self._kind = None
        self._metadata = None
        self._role_ref = None
        self._subjects = None
        self._user_names = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        self.group_names = group_names
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        self.role_ref = role_ref
        self.subjects = subjects
        self.user_names = user_names

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ClusterRoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1ClusterRoleBinding.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ClusterRoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ClusterRoleBinding.
        :type: str
        """

        self._api_version = api_version

    @property
    def group_names(self):
        """
        Gets the group_names of this V1ClusterRoleBinding.
        GroupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.

        :return: The group_names of this V1ClusterRoleBinding.
        :rtype: list[str]
        """
        return self._group_names

    @group_names.setter
    def group_names(self, group_names):
        """
        Sets the group_names of this V1ClusterRoleBinding.
        GroupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.

        :param group_names: The group_names of this V1ClusterRoleBinding.
        :type: list[str]
        """
        if group_names is None:
            raise ValueError("Invalid value for `group_names`, must not be `None`")

        self._group_names = group_names

    @property
    def kind(self):
        """
        Gets the kind of this V1ClusterRoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ClusterRoleBinding.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ClusterRoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ClusterRoleBinding.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ClusterRoleBinding.
        Standard object's metadata.

        :return: The metadata of this V1ClusterRoleBinding.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ClusterRoleBinding.
        Standard object's metadata.

        :param metadata: The metadata of this V1ClusterRoleBinding.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def role_ref(self):
        """
        Gets the role_ref of this V1ClusterRoleBinding.
        RoleRef can only reference the current namespace and the global namespace. If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role.

        :return: The role_ref of this V1ClusterRoleBinding.
        :rtype: V1ObjectReference
        """
        return self._role_ref

    @role_ref.setter
    def role_ref(self, role_ref):
        """
        Sets the role_ref of this V1ClusterRoleBinding.
        RoleRef can only reference the current namespace and the global namespace. If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role.

        :param role_ref: The role_ref of this V1ClusterRoleBinding.
        :type: V1ObjectReference
        """
        if role_ref is None:
            raise ValueError("Invalid value for `role_ref`, must not be `None`")

        self._role_ref = role_ref

    @property
    def subjects(self):
        """
        Gets the subjects of this V1ClusterRoleBinding.
        Subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy clients and servers. Thus newer clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames.

        :return: The subjects of this V1ClusterRoleBinding.
        :rtype: list[V1ObjectReference]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """
        Sets the subjects of this V1ClusterRoleBinding.
        Subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy clients and servers. Thus newer clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames.

        :param subjects: The subjects of this V1ClusterRoleBinding.
        :type: list[V1ObjectReference]
        """
        if subjects is None:
            raise ValueError("Invalid value for `subjects`, must not be `None`")

        self._subjects = subjects

    @property
    def user_names(self):
        """
        Gets the user_names of this V1ClusterRoleBinding.
        UserNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.

        :return: The user_names of this V1ClusterRoleBinding.
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        """
        Sets the user_names of this V1ClusterRoleBinding.
        UserNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy clients and servers. See Subjects for further details.

        :param user_names: The user_names of this V1ClusterRoleBinding.
        :type: list[str]
        """
        if user_names is None:
            raise ValueError("Invalid value for `user_names`, must not be `None`")

        self._user_names = user_names

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ClusterRoleBinding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
