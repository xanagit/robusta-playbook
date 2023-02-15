from robusta.api import *


class CallbackParams(ActionParams):
    title: str


@action
def iris_custom_callback(event: ExecutionBaseEvent, params: CallbackParams):
    finding = Finding(
        title="Action callback",
        source=FindingSource.PROMETHEUS,
        aggregation_key="iris_custom_callback",
    )
    finding.add_enrichment(
        [MarkdownBlock(f"Callback params : *{params.title}*")])
    event.add_finding(finding)


@action
def iris_custom_action(alert: PrometheusKubernetesAlert):
    # pod = event.get_pod()
    alert_name = None if alert.alert is None else alert.alert.labels.get(
        "alertname", "")
    if not alert_name:
        return
    else:
        alert.add_enrichment([
            HeaderBlock("IRIS Custom Paybook action"),
            MarkdownBlock("*Une erreur est survenue!*"),
            CallbackBlock(
                {
                    f'Call IRIS Custom Callback': CallbackChoice(
                        action=iris_custom_callback,
                        action_params=CallbackParams(
                            title=alert_name
                        ),
                        kubernetes_object=None
                    )
                },
            ),
            DividerBlock(),
            FileBlock("crashing-pod.log", str.encode("test de fichier de log"))
        ])
    # we have full access to the pod on which the alert fired
    # pod = event.get_pod()

    # pod_name = pod.metadata.name
    # pod_logs = pod.get_logs()
    # pod_processes = pod.exec("ps aux")

    # this is how you send data to slack or other destinations
    # event.add_enrichment([
    #     MarkdownBlock("*Une erreur est survenue!* status: " +
    #                   event.status + ", count: " + event.alerts.count()),
    #     FileBlock("crashing-pod.log", event.json)
    # ])
