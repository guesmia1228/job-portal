import graphene
import graphql_jwt

from accounts.graphql.graphql_mixins import EmployeeRegisterMixin
from jobsapp.graphql.graphql_mixins import DynamicArgsMixin, MutationMixin


class EmployeeRegister(MutationMixin, DynamicArgsMixin, EmployeeRegisterMixin, graphene.Mutation):
    __doc__ = EmployeeRegisterMixin.__doc__
    _required_args = {
        'first_name': 'String',
        'last_name': 'String',
        'email': 'String',
        'password1': 'String',
        'password2': 'String',
        'gender': 'String',
    }
