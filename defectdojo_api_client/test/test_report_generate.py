# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import defectdojo_api_client
from defectdojo_api_client.models.report_generate import ReportGenerate  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestReportGenerate(unittest.TestCase):
    """ReportGenerate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReportGenerate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.report_generate.ReportGenerate()  # noqa: E501
        if include_optional :
            return ReportGenerate(
                executive_summary = defectdojo_api_client.models.executive_summary.Executive summary(
                    engagement_name = '0', 
                    engagement_target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    engagement_target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    test_type_name = '0', 
                    test_target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_environment_name = '0', 
                    test_strategy_ref = '0', 
                    total_findings = 56, ), 
                product_type = defectdojo_api_client.models.product_type.Product type(
                    id = 56, 
                    name = '0', 
                    critical_product = True, 
                    key_product = True, 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                product = defectdojo_api_client.models.product.Product(
                    id = 56, 
                    findings_count = '0', 
                    findings_list = '0', 
                    tags = [
                        '0'
                        ], 
                    product_meta = [
                        defectdojo_api_client.models.product_meta.ProductMeta(
                            name = '0', 
                            value = '0', )
                        ], 
                    name = '0', 
                    description = '0', 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    prod_numeric_grade = -2147483648, 
                    business_criticality = 'very high', 
                    platform = 'web service', 
                    lifecycle = 'construction', 
                    origin = 'third party library', 
                    user_records = 0, 
                    revenue = '0', 
                    external_audience = True, 
                    internet_accessible = True, 
                    product_manager = 56, 
                    technical_contact = 56, 
                    team_manager = 56, 
                    prod_type = 56, 
                    authorized_users = [
                        56
                        ], 
                    regulations = [
                        56
                        ], ), 
                engagement = defectdojo_api_client.models.engagement.Engagement(
                    id = 56, 
                    tags = [
                        '0'
                        ], 
                    name = '0', 
                    description = '0', 
                    version = '0', 
                    first_contacted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    reason = '0', 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    active = True, 
                    tracker = '0', 
                    test_strategy = '0', 
                    threat_model = True, 
                    api_test = True, 
                    pen_test = True, 
                    check_list = True, 
                    status = 'Not Started', 
                    progress = '0', 
                    tmodel_path = '0', 
                    risk_path = '0', 
                    done_testing = True, 
                    engagement_type = 'Interactive', 
                    build_id = '0', 
                    commit_hash = '0', 
                    branch_tag = '0', 
                    source_code_management_uri = '0', 
                    deduplication_on_engagement = True, 
                    eng_type = 56, 
                    lead = 56, 
                    requester = 56, 
                    preset = 56, 
                    report_type = 56, 
                    product = 56, 
                    build_server = 56, 
                    source_code_management_server = 56, 
                    orchestration_engine = 56, 
                    risk_acceptance = [
                        56
                        ], ), 
                report_name = '0', 
                report_info = '0', 
                test = defectdojo_api_client.models.test.Test(
                    id = 56, 
                    tags = [
                        '0'
                        ], 
                    test_type_name = '0', 
                    title = '0', 
                    description = '0', 
                    target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    estimated_time = '0', 
                    actual_time = '0', 
                    percent_complete = -2147483648, 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    version = '0', 
                    engagement = 56, 
                    lead = 56, 
                    test_type = 56, 
                    environment = 56, 
                    notes = [
                        56
                        ], ), 
                endpoint = defectdojo_api_client.models.endpoint.Endpoint(
                    id = 56, 
                    tags = [
                        '0'
                        ], 
                    protocol = '0', 
                    host = '0', 
                    fqdn = '0', 
                    port = -2147483648, 
                    path = '0', 
                    query = '0', 
                    fragment = '0', 
                    remediated = True, 
                    product = 56, 
                    endpoint_params = [
                        56
                        ], ), 
                endpoints = [
                    defectdojo_api_client.models.endpoint.Endpoint(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        protocol = '0', 
                        host = '0', 
                        fqdn = '0', 
                        port = -2147483648, 
                        path = '0', 
                        query = '0', 
                        fragment = '0', 
                        remediated = True, 
                        product = 56, 
                        endpoint_params = [
                            56
                            ], )
                    ], 
                findings = [
                    defectdojo_api_client.models.finding.Finding(
                        id = 56, 
                        images = [
                            defectdojo_api_client.models.finding_image.FindingImage(
                                base64 = '0', 
                                caption = '0', 
                                id = 56, )
                            ], 
                        tags = [
                            '0'
                            ], 
                        accepted_risks = [
                            defectdojo_api_client.models.risk_acceptance.RiskAcceptance(
                                id = 56, 
                                name = '0', 
                                path = '0', 
                                accepted_by = '0', 
                                expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                compensating_control = '0', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                owner = 56, 
                                accepted_findings = [
                                    56
                                    ], 
                                notes = [
                                    56
                                    ], )
                            ], 
                        push_to_jira = True, 
                        age = 56, 
                        sla_days_remaining = 56, 
                        title = '0', 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        cwe = -2147483648, 
                        cve = 'a', 
                        url = '0', 
                        severity = '0', 
                        description = '0', 
                        mitigation = '0', 
                        impact = '0', 
                        steps_to_reproduce = '0', 
                        severity_justification = '0', 
                        references = '0', 
                        is_template = True, 
                        active = True, 
                        verified = True, 
                        false_p = True, 
                        duplicate = True, 
                        out_of_scope = True, 
                        under_review = True, 
                        under_defect_review = True, 
                        is_mitigated = True, 
                        thread_id = 56, 
                        mitigated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        numerical_severity = '0', 
                        last_reviewed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        line_number = '0', 
                        sourcefilepath = '0', 
                        sourcefile = '0', 
                        param = '0', 
                        payload = '0', 
                        hash_code = '0', 
                        line = -2147483648, 
                        file_path = '0', 
                        component_name = '0', 
                        component_version = '0', 
                        static_finding = True, 
                        dynamic_finding = True, 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        jira_creation = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        jira_change = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scanner_confidence = 56, 
                        unique_id_from_tool = '0', 
                        sast_source_object = '0', 
                        sast_sink_object = '0', 
                        sast_source_line = -2147483648, 
                        sast_source_file_path = '0', 
                        nb_occurences = -2147483648, 
                        test = 56, 
                        duplicate_finding = 56, 
                        review_requested_by = 56, 
                        defect_review_requested_by = 56, 
                        mitigated_by = 56, 
                        reporter = 56, 
                        last_reviewed_by = 56, 
                        sonarqube_issue = 56, 
                        endpoints = [
                            56
                            ], 
                        reviewers = [
                            56
                            ], 
                        notes = [
                            defectdojo_api_client.models.note.Note(
                                id = 56, 
                                author = defectdojo_api_client.models.author.Author(
                                    id = 56, 
                                    username = 'a', 
                                    first_name = '0', 
                                    last_name = '0', 
                                    email = '0', 
                                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                editor = defectdojo_api_client.models.author.Author(
                                    id = 56, 
                                    username = 'a', 
                                    first_name = '0', 
                                    last_name = '0', 
                                    email = '0', 
                                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                history = [
                                    defectdojo_api_client.models.note_history.NoteHistory(
                                        id = 56, 
                                        current_editor = defectdojo_api_client.models.author.Author(
                                            id = 56, 
                                            username = 'a', 
                                            first_name = '0', 
                                            last_name = '0', 
                                            email = '0', 
                                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                        data = '0', 
                                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        note_type = 56, )
                                    ], 
                                entry = '0', 
                                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                private = True, 
                                edited = True, 
                                edit_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                note_type = 56, )
                            ], 
                        found_by = [
                            56
                            ], )
                    ], 
                user = defectdojo_api_client.models.author.Author(
                    id = 56, 
                    username = 'a', 
                    first_name = '0', 
                    last_name = '0', 
                    email = '0', 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                team_name = '0', 
                title = '0', 
                user_id = 56, 
                host = '0', 
                finding_images = [
                    defectdojo_api_client.models.finding_to_finding_images.FindingToFindingImages(
                        finding_id = 56, 
                        images = [
                            defectdojo_api_client.models.finding_image.FindingImage(
                                base64 = '0', 
                                caption = '0', 
                                id = 56, )
                            ], )
                    ], 
                finding_notes = [
                    defectdojo_api_client.models.finding_to_notes.FindingToNotes(
                        finding_id = 56, 
                        notes = [
                            defectdojo_api_client.models.note.Note(
                                id = 56, 
                                author = defectdojo_api_client.models.author.Author(
                                    id = 56, 
                                    username = 'a', 
                                    first_name = '0', 
                                    last_name = '0', 
                                    email = '0', 
                                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                editor = defectdojo_api_client.models.author.Author(
                                    id = 56, 
                                    username = 'a', 
                                    first_name = '0', 
                                    last_name = '0', 
                                    email = '0', 
                                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                history = [
                                    defectdojo_api_client.models.note_history.NoteHistory(
                                        id = 56, 
                                        current_editor = defectdojo_api_client.models.author.Author(
                                            id = 56, 
                                            username = 'a', 
                                            first_name = '0', 
                                            last_name = '0', 
                                            email = '0', 
                                            last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                        data = '0', 
                                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        note_type = 56, )
                                    ], 
                                entry = '0', 
                                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                private = True, 
                                edited = True, 
                                edit_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                note_type = 56, )
                            ], )
                    ]
            )
        else :
            return ReportGenerate(
                executive_summary = defectdojo_api_client.models.executive_summary.Executive summary(
                    engagement_name = '0', 
                    engagement_target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    engagement_target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    test_type_name = '0', 
                    test_target_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_target_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    test_environment_name = '0', 
                    test_strategy_ref = '0', 
                    total_findings = 56, ),
                report_name = '0',
                report_info = '0',
                team_name = '0',
                title = '0',
                user_id = 56,
                host = '0',
        )

    def testReportGenerate(self):
        """Test ReportGenerate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()