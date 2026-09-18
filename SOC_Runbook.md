# SOC Detection & Response Playbook
## SSL/TLS Configuration Weaknesses — Cleaning Services Organization

### 1. Objective
Detect suspicious SSL/TLS configuration activity and provide an analyst workflow for triage, containment, notification, and remediation.

### 2. Detection Logic
The detection rule flags log entries containing:
- TLS 1.0
- TLS 1.1
- Known weak/deprecated cipher patterns such as 3DES, DES-CBC3-SHA, and AES128-SHA

TLS 1.0 and TLS 1.1 are deprecated by IETF RFC 8996. Modern deployments should migrate away from these versions and use current TLS configurations.

### 3. Detection Rule
The Python rule reads sample_logs.txt and generates an alert when a suspicious TLS version or cipher pattern is found.

### 4. Alert Triage Checklist
When an alert fires, the SOC analyst should:

1. Identify the source IP.
2. Identify the destination server/service.
3. Check the TLS version and cipher used.
4. Check whether the connection was successful or rejected.
5. Review whether the source generated repeated alerts.
6. Check related authentication, firewall, web-server, and endpoint logs.
7. Determine whether the activity is expected, caused by an old system, or suspicious.
8. Escalate repeated or unexplained activity.

### 5. Incident Response Playbook

#### Detection & Analysis
- Validate the alert against the original log.
- Record timestamp, source IP, destination, TLS version, cipher, and status.
- Determine whether the event is isolated or repeated.

#### Containment
- If activity is confirmed as suspicious, restrict the affected source according to the organization's security policy.
- Preserve relevant logs before making changes.
- Avoid disrupting legitimate business systems without authorization.

#### Notification
Notify:
- SOC/security team
- System or network administrator responsible for the affected service
- Incident response lead when escalation criteria are met
- Relevant management/business owner when business impact is identified

#### Remediation
- Disable TLS 1.0 and TLS 1.1 where operationally possible.
- Remove weak/deprecated cipher suites.
- Configure approved modern TLS versions and cipher suites.
- Update affected server software or TLS libraries.
- Test the service after configuration changes.
- Document the change and its business impact.

#### Recovery
- Confirm that legitimate clients can establish secure connections.
- Monitor TLS-related logs for recurrence.
- Close the incident only after validation and documentation.

### 6. Test Results

#### Test 1 — Suspicious Sample
Result: PASS

The rule detected 4 suspicious entries:
- 3 alerts from source 10.10.20.45
- 1 alert from source 10.10.20.60

The detected events contained TLS 1.0/TLS 1.1 and weak cipher patterns.

#### Test 2 — Benign Sample
Result: PASS

The benign sample contained TLS 1.2 and TLS 1.3 connections using modern cipher patterns.

Result:
- Alerts generated: 0
- Normal traffic was not flagged.

### 7. Detection Coverage
This rule provides basic coverage for:
- TLS 1.0 usage
- TLS 1.1 usage
- Selected weak/deprecated cipher patterns
- Repeated suspicious connections visible in logs

### 8. Known Blind Spots
The rule does not detect every possible TLS weakness.

Limitations include:
- It depends on the log containing TLS version and cipher information.
- It does not inspect packet contents.
- It does not validate certificates.
- It does not detect every weak cipher.
- It does not prove that an attack was successful.
- Real production logs may use different field names and formats.
- Additional tuning would be required before production deployment.

### 9. False Positive Considerations
Some old or legacy systems may legitimately attempt older TLS versions. The analyst should verify the source, owner, business purpose, and connection history before escalating.

### 10. Lab Safety
All testing was performed using controlled sample logs. No unauthorized systems were targeted.

### 11. Metrics
MTTD (Mean Time to Detect): Time between the suspicious event occurring and the SOC detecting it.

MTTR (Mean Time to Respond/Resolve): Time taken by the SOC to respond to and resolve the incident.

### 12. References
- IETF RFC 8996 — Deprecating TLS 1.0 and TLS 1.1
- NIST SP 800-61 — Computer Security Incident Handling Guide
