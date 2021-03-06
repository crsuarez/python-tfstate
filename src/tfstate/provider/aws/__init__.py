# -*- coding: utf-8 -*-

from tfstate.provider.aws.base import AwsResource
from tfstate.provider.aws.aws_eip import AwsEipResource
from tfstate.provider.aws.aws_elb import AwsElbResource
from tfstate.provider.aws.aws_iam_server_certificate import AwsIamServerCertificateResource
from tfstate.provider.aws.aws_internet_gateway import AwsInternetGatewayResource
from tfstate.provider.aws.aws_route_table import AwsRouteTableResource
from tfstate.provider.aws.aws_route_table_association import AwsRouteTableAssociationResource
from tfstate.provider.aws.aws_subnet import AwsSubnetResource
from tfstate.provider.aws.aws_vpc import AwsVpcResource, AwsVpcPeeringConnectionResource
from tfstate.provider.aws.aws_key_pair import AwsKeyPairResource
from tfstate.provider.aws.aws_instance import AwsInstanceResource
from tfstate.provider.aws.aws_security_group import AwsSecurityGroupResource, AwsSecurityGroupRuleResource
from tfstate.provider.aws.aws_nat_gateway import AwsNatGatewayResource
from tfstate.provider.aws.aws_route import AwsRouteResource
from tfstate.provider.aws.aws_eip_association import AwsEipAssociation
from tfstate.provider.aws.aws_route53_record import AwsRoute53RecordResource
from tfstate.provider.aws.data_aws_ami import DataAwsAmiResource
from tfstate.provider.aws.data_aws_caller_identity import DataAwsCallerIdentityResource
from tfstate.provider.aws.data_aws_security_group import DataAwsSecurityGroupResource
from tfstate.provider.aws.aws_autoscaling_group import AwsAutoScalingGroupResource
from tfstate.provider.aws.aws_autoscaling_policy import AwsAutoScalingPolicyResource
from tfstate.provider.aws.aws_cloudwatch_metric_alarm import AwsCloudWatchMetricAlarmResource
from tfstate.provider.aws.aws_elasticache_replication_group import AwsElasticCacheReplicationGroupResource
from tfstate.provider.aws.aws_elasticache_subnet_group import AwsElasticCacheSubnetGroupResource
from tfstate.provider.aws.aws_lambda_function import AwsLambdaFunctionResource
from tfstate.provider.aws.aws_lambda_permission import AwsLambdaPermissionResource
from tfstate.provider.aws.aws_launch_configuration import AwsLaunchConfigurationResource
from tfstate.provider.aws.aws_sns_topic import AwsSnsTopicResource
from tfstate.provider.aws.aws_sns_topic_subscription import AwsSnsTopicSubscriptionResource
from tfstate.provider.aws.aws_lb_ssl_negotiation_policy import AwsLBSSLNegotiationPolicyResource
from tfstate.provider.aws.aws_proxy_protocol_policy import AwsProxyProtocolPolicyResource
