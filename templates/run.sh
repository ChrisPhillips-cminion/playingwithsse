oc process -f templates/jmeter-bc.yaml \
    -p APP_NAMESPACE=sse \
    -p APPLICATION_NAME=sse | oc apply -f -

oc process -f templates/jmeter-dc.yaml \
    -p APP_NAMESPACE=sse \
    -p APPLICATION_NAME=sse  | oc apply -f -
