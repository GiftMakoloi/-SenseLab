import json
from pathlib import Path

import pandas as pd
import streamlit as st

from engine.risk import calculate_risk
from engine.scenarios import load_scenarios
from engine.scoring import calculate_score


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="SenseLab",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 1.15rem;
        opacity: 0.75;
        margin-bottom: 2rem;
    }

    .security-banner {
        padding: 1rem;
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 10px;
        margin-bottom: 1.5rem;
    }

    .metric-card {
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.12);
    }

    .finding-critical {
        border-left: 5px solid #ff4b4b;
        padding: 1rem;
    }

    .finding-high {
        border-left: 5px solid #ff8c42;
        padding: 1rem;
    }

    .finding-medium {
        border-left: 5px solid #ffd166;
        padding: 1rem;
    }

    .finding-low {
        border-left: 5px solid #4cc9f0;
        padding: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------

if "selected_scenario" not in st.session_state:
    st.session_state.selected_scenario = None

if "findings" not in st.session_state:
    st.session_state.findings = []

if "completed_modules" not in st.session_state:
    st.session_state.completed_modules = set()

if "mode" not in st.session_state:
    st.session_state.mode = "Training Mode"


# ---------------------------------------------------------
# Data
# ---------------------------------------------------------

scenarios = load_scenarios()


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.title("SenseLab")

    st.caption(
        "Web Application Security Assessment "
        "& Penetration Testing Training Laboratory"
    )

    st.divider()

    st.session_state.mode = st.radio(
        "Assessment Mode",
        ["Training Mode", "Assessment Mode"],
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Scenario",
            "Reconnaissance",
            "Network & DNS",
            "HTTP Analysis",
            "API Security",
            "Vulnerability Lab",
            "Risk Assessment",
            "Remediation",
            "Retesting",
            "Security Report",
            "Methodology",
        ],
    )

    st.divider()

    st.warning(
        "AUTHORIZED LAB ONLY\n\n"
        "All targets in SenseLab are simulated. "
        "Do not use security-testing techniques against "
        "systems without explicit authorization."
    )


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def mark_complete(module):
    st.session_state.completed_modules.add(module)


def add_finding(finding):
    existing = [
        item["id"] for item in st.session_state.findings
    ]

    if finding["id"] not in existing:
        st.session_state.findings.append(finding)


def get_selected_scenario():

    if not st.session_state.selected_scenario:
        return None

    return next(
        (
            scenario
            for scenario in scenarios
            if scenario["id"]
            == st.session_state.selected_scenario
        ),
        None,
    )


scenario = get_selected_scenario()


# ---------------------------------------------------------
# Dashboard
# ---------------------------------------------------------

if page == "Dashboard":

    st.markdown(
        '<div class="main-title">SenseLab</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="subtitle">'
        "Web Application Security Assessment & "
        "Penetration Testing Training Laboratory"
        "</div>",
        unsafe_allow_html=True,
    )

    st.info(
        "Think like an attacker. Build like an engineer. "
        "Defend like a security professional."
    )

    st.markdown(
        """
        <div class="security-banner">
        <strong>AUTHORIZED SECURITY LAB</strong><br>
        SenseLab uses simulated targets and controlled
        scenarios for cybersecurity education and
        security-assessment training.
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Scenarios",
            len(scenarios),
        )

    with col2:
        st.metric(
            "Modules Completed",
            len(st.session_state.completed_modules),
        )

    with col3:
        st.metric(
            "Findings",
            len(st.session_state.findings),
        )

    with col4:

        score = calculate_score(
            st.session_state.completed_modules,
            st.session_state.findings,
        )

        st.metric(
            "Assessment Score",
            f"{score}/100",
        )

    st.divider()

    st.subheader("Assessment Lifecycle")

    stages = [
        "Scope",
        "Reconnaissance",
        "Attack Surface",
        "HTTP/API Analysis",
        "Vulnerability Identification",
        "Risk Assessment",
        "Remediation",
        "Retesting",
        "Reporting",
    ]

    cols = st.columns(3)

    for index, stage in enumerate(stages):

        with cols[index % 3]:

            st.markdown(
                f"""
                **{index + 1}. {stage}**
                """
            )

    st.divider()

    st.subheader("How SenseLab Works")

    st.write(
        """
        SenseLab provides controlled cybersecurity scenarios
        where users investigate simulated applications,
        analyse technical evidence, identify security
        weaknesses, assess risk, recommend remediation and
        perform simulated retesting.
        """
    )

    st.write(
        """
        The objective is not to memorise vulnerability names.
        The objective is to develop the reasoning process
        required to investigate how applications behave and
        determine where security controls may fail.
        """
    )


# ---------------------------------------------------------
# Scenario
# ---------------------------------------------------------

elif page == "Scenario":

    st.title("Security Assessment Scenario")

    st.write(
        "Select an authorized laboratory scenario."
    )

    for item in scenarios:

        with st.container(border=True):

            st.subheader(item["name"])

            st.write(item["description"])

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("**Organization**")
                st.write(item["organization"])

                st.markdown("**Target**")
                st.code(item["target"])

            with col2:

                st.markdown("**Environment**")
                st.write(item["environment"])

                st.markdown("**Difficulty**")
                st.write(item["difficulty"])

            if st.button(
                f"Select {item['name']}",
                key=f"select_{item['id']}",
            ):

                st.session_state.selected_scenario = item["id"]
                st.session_state.findings = []
                st.session_state.completed_modules = set()

                st.success(
                    f"Scenario selected: {item['name']}"
                )

                st.rerun()

    if scenario:

        st.divider()

        st.subheader("Current Scope")

        st.write(scenario["objective"])

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### In Scope")

            for item in scenario["scope"]["in_scope"]:
                st.write(f"- {item}")

        with col2:

            st.markdown("### Out of Scope")

            for item in scenario["scope"]["out_of_scope"]:
                st.write(f"- {item}")


# ---------------------------------------------------------
# Reconnaissance
# ---------------------------------------------------------

elif page == "Reconnaissance":

    st.title("Reconnaissance")

    if not scenario:

        st.warning("Select a scenario first.")

    else:

        st.write(
            """
            Review the simulated target information and
            identify components that could form part of
            the application's attack surface.
            """
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Target",
                scenario["target"],
            )

        with col2:
            st.metric(
                "Simulated IP",
                scenario["ip"],
            )

        with col3:
            st.metric(
                "Application",
                scenario["application"],
            )

        st.subheader("Discovered Services")

        services = pd.DataFrame(
            scenario["services"]
        )

        st.dataframe(
            services,
            use_container_width=True,
            hide_index=True,
        )

        st.subheader("Reconnaissance Questions")

        answers = []

        answers.append(
            st.text_input(
                "What is the simulated target IP?"
            )
        )

        answers.append(
            st.text_input(
                "What application is being assessed?"
            )
        )

        if st.button("Submit Reconnaissance"):

            correct = 0

            if answers[0].strip() == scenario["ip"]:
                correct += 1

            if (
                answers[1].strip().lower()
                == scenario["application"].lower()
            ):
                correct += 1

            if correct == 2:

                mark_complete("Reconnaissance")

                st.success(
                    "Reconnaissance assessment completed."
                )

            else:

                st.error(
                    f"{correct}/2 answers correct."
                )


# ---------------------------------------------------------
# Network & DNS
# ---------------------------------------------------------

elif page == "Network & DNS":

    st.title("Network & DNS Analysis")

    st.subheader("RFC1918 Private IPv4 Addressing")

    st.write(
        """
        RFC1918 defines private IPv4 address space commonly
        used inside private networks.
        """
    )

    ranges = pd.DataFrame(
        {
            "Range": [
                "10.0.0.0/8",
                "172.16.0.0/12",
                "192.168.0.0/16",
            ],
            "Purpose": [
                "Private IPv4",
                "Private IPv4",
                "Private IPv4",
            ],
        }
    )

    st.dataframe(
        ranges,
        use_container_width=True,
        hide_index=True,
    )

    ip = st.text_input(
        "Enter an IPv4 address",
        placeholder="192.168.1.25",
    )

    if st.button("Classify Address"):

        import ipaddress

        try:

            address = ipaddress.ip_address(ip)

            private = address.is_private

            if private:

                st.success(
                    f"{ip} is classified as a private address."
                )

            else:

                st.info(
                    f"{ip} is not within RFC1918 private IPv4 space."
                )

        except ValueError:

            st.error("Invalid IPv4 address.")

    st.divider()

    st.subheader("Simulated DNS Records")

    dns_records = pd.DataFrame(
        scenario["dns_records"]
        if scenario
        else []
    )

    if not dns_records.empty:

        st.dataframe(
            dns_records,
            use_container_width=True,
            hide_index=True,
        )

    st.caption(
        "DNS information displayed by SenseLab is simulated "
        "and is not retrieved from external domains."
    )

    if st.button("Complete Network & DNS Module"):

        mark_complete("Network & DNS")

        st.success(
            "Network and DNS module completed."
        )


# ---------------------------------------------------------
# HTTP Analysis
# ---------------------------------------------------------

elif page == "HTTP Analysis":

    st.title("HTTP Analysis")

    if not scenario:

        st.warning("Select a scenario first.")

    else:

        st.subheader("Simulated HTTP Request")

        st.code(
            scenario["http"]["request"],
            language="http",
        )

        st.subheader("Simulated HTTP Response")

        st.code(
            scenario["http"]["response"],
            language="http",
        )

        st.subheader("Analysis")

        selected = st.multiselect(
            "Which elements should be investigated?",
            [
                "HTTP method",
                "Parameters",
                "Cookies",
                "Authorization",
                "Response headers",
                "Status code",
                "Information disclosure",
                "Content type",
            ],
        )

        if st.button("Submit HTTP Analysis"):

            required = {
                "HTTP method",
                "Parameters",
                "Cookies",
                "Authorization",
                "Response headers",
                "Status code",
            }

            if required.issubset(set(selected)):

                mark_complete("HTTP Analysis")

                st.success(
                    "HTTP analysis completed."
                )

            else:

                missing = required - set(selected)

                st.warning(
                    "Consider investigating: "
                    + ", ".join(missing)
                )


# ---------------------------------------------------------
# API Security
# ---------------------------------------------------------

elif page == "API Security":

    st.title("API Security Assessment")

    if not scenario:

        st.warning("Select a scenario first.")

    else:

        st.write(
            """
            The API environment below is simulated.
            Investigate the behaviour of resources and
            authorization controls.
            """
        )

        for endpoint in scenario["api_endpoints"]:

            with st.container(border=True):

                st.code(
                    f"{endpoint['method']} "
                    f"{endpoint['path']}"
                )

                st.write(
                    endpoint["description"]
                )

                if st.button(
                    "Inspect Response",
                    key=endpoint["id"],
                ):

                    st.code(
                        endpoint["response"],
                        language="json",
                    )

        st.divider()

        st.subheader("Security Question")

        answer = st.radio(
            """
            A user authenticated as a normal analyst can
            retrieve another user's record by changing a
            resource identifier. What should be investigated?
            """,
            [
                "DNS configuration",
                "Authorization and access control",
                "CSS configuration",
                "Browser compatibility",
            ],
        )

        if st.button("Submit API Finding"):

            if answer == "Authorization and access control":

                finding = {
                    "id": "F001",
                    "title": "Broken Access Control",
                    "category": "Authorization",
                    "severity": "High",
                    "likelihood": 4,
                    "impact": 5,
                    "exploitability": 4,
                    "status": "Open",
                    "description": (
                        "The simulated API permits access "
                        "to a resource without adequately "
                        "verifying authorization."
                    ),
                    "remediation": (
                        "Enforce server-side authorization "
                        "and verify resource ownership."
                    ),
                }

                add_finding(finding)

                mark_complete("API Security")

                st.success(
                    "Correct. Potential broken access "
                    "control identified."
                )

            else:

                st.error(
                    "That does not address the observed "
                    "resource-access behaviour."
                )


# ---------------------------------------------------------
# Vulnerability Lab
# ---------------------------------------------------------

elif page == "Vulnerability Lab":

    st.title("Vulnerability Laboratory")

    if not scenario:

        st.warning("Select a scenario first.")

    else:

        for vulnerability in scenario["vulnerabilities"]:

            with st.container(border=True):

                st.subheader(
                    vulnerability["title"]
                )

                st.write(
                    vulnerability["description"]
                )

                answer = st.selectbox(
                    "Classify this finding",
                    vulnerability["options"],
                    key=vulnerability["id"],
                )

                if st.button(
                    "Submit Classification",
                    key=f"submit_{vulnerability['id']}",
                ):

                    if (
                        answer
                        == vulnerability["correct_answer"]
                    ):

                        finding = {
                            "id": vulnerability["id"],
                            "title": vulnerability["title"],
                            "category": vulnerability["category"],
                            "severity": vulnerability["severity"],
                            "likelihood": vulnerability[
                                "likelihood"
                            ],
                            "impact": vulnerability["impact"],
                            "exploitability": vulnerability[
                                "exploitability"
                            ],
                            "status": "Open",
                            "description": vulnerability[
                                "description"
                            ],
                            "remediation": vulnerability[
                                "remediation"
                            ],
                        }

                        add_finding(finding)

                        st.success(
                            "Correct vulnerability classification."
                        )

                    else:

                        st.error(
                            "Incorrect classification. "
                            "Review the evidence."
                        )

        if st.button(
            "Complete Vulnerability Module"
        ):

            mark_complete("Vulnerability Lab")

            st.success(
                "Vulnerability laboratory completed."
            )


# ---------------------------------------------------------
# Risk Assessment
# ---------------------------------------------------------

elif page == "Risk Assessment":

    st.title("Risk Assessment")

    if not st.session_state.findings:

        st.info(
            "Identify at least one finding before performing "
            "risk assessment."
        )

    else:

        results = []

        for finding in st.session_state.findings:

            risk = calculate_risk(
                finding["likelihood"],
                finding["impact"],
                finding["exploitability"],
            )

            results.append(
                {
                    "ID": finding["id"],
                    "Finding": finding["title"],
                    "Severity": finding["severity"],
                    "Risk Score": risk["score"],
                    "Risk Level": risk["level"],
                }
            )

        dataframe = pd.DataFrame(results)

        st.dataframe(
            dataframe,
            use_container_width=True,
            hide_index=True,
        )

        for item in results:

            st.metric(
                item["Finding"],
                f"{item['Risk Score']}/100",
                item["Risk Level"],
            )

        if st.button(
            "Complete Risk Assessment"
        ):

            mark_complete("Risk Assessment")

            st.success(
                "Risk assessment completed."
            )


# ---------------------------------------------------------
# Remediation
# ---------------------------------------------------------

elif page == "Remediation":

    st.title("Remediation")

    if not st.session_state.findings:

        st.info(
            "No findings are currently available."
        )

    else:

        for finding in st.session_state.findings:

            with st.container(border=True):

                st.subheader(
                    finding["title"]
                )

                st.write(
                    finding["description"]
                )

                st.markdown("**Recommended remediation**")

                st.write(
                    finding["remediation"]
                )

                confirmed = st.checkbox(
                    "I understand the recommended remediation.",
                    key=f"remediation_{finding['id']}",
                )

                if confirmed:

                    finding["status"] = "Remediation Planned"

                    st.success(
                        "Remediation recorded."
                    )

        if st.button(
            "Complete Remediation Module"
        ):

            mark_complete("Remediation")

            st.success(
                "Remediation module completed."
            )


# ---------------------------------------------------------
# Retesting
# ---------------------------------------------------------

elif page == "Retesting":

    st.title("Retesting")

    if not st.session_state.findings:

        st.info(
            "No findings are available for retesting."
        )

    else:

        for finding in st.session_state.findings:

            st.subheader(
                finding["title"]
            )

            if finding["status"] == "Open":

                st.code(
                    "BEFORE REMEDIATION\n"
                    "HTTP 200 OK\n"
                    "Unauthorized resource returned"
                )

                st.info(
                    "Apply the recommended remediation "
                    "before performing the simulated retest."
                )

            else:

                st.code(
                    "AFTER REMEDIATION\n"
                    "HTTP 403 Forbidden\n"
                    "Access denied"
                )

                if st.button(
                    f"Retest {finding['id']}",
                    key=f"retest_{finding['id']}",
                ):

                    finding["status"] = "Resolved"

                    st.success(
                        "Retest passed. Finding resolved."
                    )

        if st.button(
            "Complete Retesting Module"
        ):

            mark_complete("Retesting")

            st.success(
                "Retesting module completed."
            )


# ---------------------------------------------------------
# Security Report
# ---------------------------------------------------------

elif page == "Security Report":

    st.title("Security Assessment Report")

    if not scenario:

        st.warning("Select a scenario first.")

    else:

        st.subheader("Executive Summary")

        st.write(
            f"""
            A controlled security assessment was performed
            against the simulated {scenario['application']}
            environment.

            The assessment investigated the application's
            simulated attack surface, HTTP behaviour, API
            security controls and application-level
            vulnerabilities.
            """
        )

        st.subheader("Scope")

        for item in scenario["scope"]["in_scope"]:
            st.write(f"- {item}")

        st.subheader("Findings")

        if not st.session_state.findings:

            st.info(
                "No findings have been recorded."
            )

        else:

            for finding in st.session_state.findings:

                st.markdown(
                    f"""
                    ### {finding['id']} — {finding['title']}

                    **Category:** {finding['category']}

                    **Severity:** {finding['severity']}

                    **Status:** {finding['status']}

                    **Description:**  
                    {finding['description']}

                    **Recommendation:**  
                    {finding['remediation']}
                    """
                )

        st.subheader("Assessment Score")

        score = calculate_score(
            st.session_state.completed_modules,
            st.session_state.findings,
        )

        st.metric(
            "SenseLab Assessment Score",
            f"{score}/100",
        )

        report = {
            "scenario": scenario,
            "findings": st.session_state.findings,
            "score": score,
        }

        report_json = json.dumps(
            report,
            indent=2,
        )

        st.download_button(
            "Export Assessment Data",
            data=report_json,
            file_name="senselab_assessment.json",
            mime="application/json",
        )


# ---------------------------------------------------------
# Methodology
# ---------------------------------------------------------

elif page == "Methodology":

    st.title("Security Assessment Methodology")

    st.write(
        """
        SenseLab follows a simplified security-assessment
        methodology designed for controlled educational
        environments.
        """
    )

    stages = {
        "1. Scope": (
            "Understand the authorized target and "
            "rules of engagement."
        ),
        "2. Reconnaissance": (
            "Collect simulated information about "
            "the target environment."
        ),
        "3. Attack Surface": (
            "Identify application components and "
            "potential areas requiring investigation."
        ),
        "4. HTTP/API Analysis": (
            "Examine application requests, responses "
            "and API behaviour."
        ),
        "5. Vulnerability Identification": (
            "Use technical evidence to identify "
            "potential security weaknesses."
        ),
        "6. Risk Assessment": (
            "Evaluate likelihood, impact and "
            "exploitability."
        ),
        "7. Remediation": (
            "Recommend controls that address "
            "the underlying security issue."
        ),
        "8. Retesting": (
            "Validate whether remediation successfully "
            "addresses the finding."
        ),
        "9. Reporting": (
            "Document technical findings and "
            "recommendations."
        ),
    }

    for title, description in stages.items():

        with st.container(border=True):

            st.subheader(title)

            st.write(description)

    st.divider()

    st.subheader("Responsible Security Testing")

    st.warning(
        """
        Security testing must always be authorized.

        SenseLab intentionally uses simulated targets and
        controlled scenarios so that learners can practice
        security reasoning without interacting with systems
        they do not own or have permission to assess.
        """
    )
