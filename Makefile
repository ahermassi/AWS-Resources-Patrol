S3_BUCKET ?= anouer-demo
AWS_REGION ?= us-east-1
SENDER := hermassi.anouer@gmail.com
RECIPIENTS := hermassi.anouer@gmail.com

package:
	mkdir -p build/services
	mkdir -p build/utils
	mkdir -p build/config
	cp -R *.py ./build/
	cp -R ./utils/*.py ./build/utils/
	cp -R ./config/* ./build/config/
	cp -R ./services/*.py ./build/services/
	aws cloudformation package --template-file sam.yaml --s3-bucket ${S3_BUCKET} --output-template-file build/template-lambda.yml
	aws s3 cp build/template-lambda.yml 's3://${S3_BUCKET}/template-lambda.yml'

deploy:
	aws cloudformation deploy --template-file build/template-lambda.yml --region ${AWS_REGION} \
		--stack-name "aws-resources-patrol" --capabilities CAPABILITY_IAM --parameter-overrides \
		SENDER=${SENDER} RECIPIENTS="${RECIPIENTS}" PROJECT=aws-resources-patrol \
			AWSREGION=${AWS_REGION} --no-fail-on-empty-changeset