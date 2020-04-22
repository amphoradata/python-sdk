from logging import getLogger
logger = getLogger('amphora_access.py')

import amphora_api_client as api
from amphora.base import Base


class AmphoraAccess(Base):
    def __init__(self, apiClient: api.ApiClient, amphora_id: str):
        self._id = amphora_id
        Base.__init__(self, apiClient)

    def get_organisation_rules(self):
        """
        Returns a list of access rules applied to this Amphora.
        returns:
            
        """

    # Access Rules
    def create_organisation_rule(
            self,
            organisation_id: str,
            allow_or_deny: str = 'Deny',
            priority: int = 100) -> api.OrganisationAccessRule:
        """
        Creates a rule by Organisation on this Amphora
        params:
            organisation_id: str          The organisation to which to apply the rule.
            allow_or_deny: str            Allow or Deny.
            priority: int                 Higher overrides lower.
        returns:
            amphora_api_client.OrganisationAccessRule      
        """
        rule = api.OrganisationAccessRule(organisation_id=organisation_id,
                                          allow_or_deny=allow_or_deny,
                                          priority=priority)
        return self.amphoraeApi.amphorae_access_controls_create_for_organisation(
            id=self._id, organisation_access_rule=rule)

    def create_user_rule(self,
                         username: str,
                         allow_or_deny: str = 'Deny',
                         priority: int = 100) -> api.UserAccessRule:
        """
        Creates a rule by Organisation on this Amphora
        params:
            username: str          The user name of the user to which to apply the rule.
            allow_or_deny: str            Allow or Deny.
            priority: int                 Higher overrides lower.
        returns:
            amphora_api_client.UserAccessRule      
        """
        rule = api.UserAccessRule(username=username,
                                  allow_or_deny=allow_or_deny,
                                  priority=priority)
        return self.amphoraeApi.amphorae_access_controls_create_for_user(
            id=self._id, user_access_rule=rule)

    def delete_rule(self, rule_id: str):
        """
        Creates a rule by Organisation on this Amphora
        params:
            username: str          The user name of the user to which to apply the rule.
            allow_or_deny: str            Allow or Deny.
            priority: int                 Higher overrides lower.
        returns:
            amphora_api_client.UserAccessRule      
        """
        return self.amphoraeApi.amphorae_access_controls_delete(
            id=self._id, rule_id=rule_id)
