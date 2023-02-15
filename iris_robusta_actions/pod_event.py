from robusta.api import *


@action
def iris_custom_action(event: PodEvent):
    # pod = event.get_pod()
    event.add_enrichment([
        MarkdownBlock("*Une erreur est survenue!*"),
        FileBlock("crashing-pod.log", "test de fichier de log")
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
