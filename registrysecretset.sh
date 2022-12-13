"""
#!/bin/bash
ACCOUNT="<AWS_ACCOUNT_ID>"
REGION="<REGION>"
SECRET_NAME="<SECRETE_NAME>"
EMAIL="<SOME_DUMMY_EMAIL>"

TOKEN=`/usr/local/bin/aws ecr --region=$REGION --profile <AWS_PROFILE> get-authorization-token --output text --query authorizationData[].authorizationToken | base64 -d | cut -d: -f2`

kubectl delete secret --ignore-not-found $SECRET_NAME
kubectl create secret docker-registry $SECRET_NAME \
 --docker-server=https://${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com \
 --docker-username=AWS \
 --docker-password="${TOKEN}" \
 --docker-email="${EMAIL}"
"""

# KUBECTL='kubectl --dry-run=client'
KUBECTL='kubectl'

AWS_DEFAULT_REGION=ap-south-1

EXISTS=$($KUBECTL get secret "$ENVIRONMENT-aws-ecr-$AWS_DEFAULT_REGION" | tail -n 1 | cut -d ' ' -f 1)
if [ "$EXISTS" = "$ENVIRONMENT-aws-ecr-$AWS_DEFAULT_REGION" ]; then
  echo "Secret exists, deleting"
  $KUBECTL delete secrets "$ENVIRONMENT-aws-ecr-$AWS_DEFAULT_REGION"
fi

PASS=$(aws ecr get-login-password --region $AWS_DEFAULT_REGION)
$KUBECTL create secret docker-registry $ENVIRONMENT-aws-ecr-$AWS_DEFAULT_REGION \
    --docker-server=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com \
    --docker-username=AWS \
    --docker-password=$PASS \
    --docker-email=infra@setu.co --namespace collect

