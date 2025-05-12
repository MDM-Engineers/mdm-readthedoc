# I. Theory

- **1/ What is autopilot user-driven mode**
    
    **Autopilot User-Driven Mode** lets end users set up their devices themselves with minimal IT involvement. After turning on the device and signing in, the device automatically joins the organization, enrolls in Intune, and applies company policies — ready for use.
    
- **2/ When do we use user-driven mode**
    - The Device will be **delivered directly to the end users** without IT intervention
        - Requires no interaction from IT team/OEM/reseller.
    - The device will be used primarily by **a single user**
    - Doesn't require [**TPM attestation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/tpm-key-attestation)** so works on physical devices and VMs.
        - Because user-driven does not require TPM so we can leverage this mode to test enrollment status or creating VMs for testing an autopilot process