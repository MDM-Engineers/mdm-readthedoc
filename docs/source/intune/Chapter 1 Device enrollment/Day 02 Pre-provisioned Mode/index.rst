
Day 2-2 Pre-provisioned Mode
==========================================

📌 Today we will discuss **Windows Autopilot with Pre-provisioned Mode**.
This article provides a theoretical overview and step-by-step guide.

Reference: https://learn.microsoft.com/en-us/autopilot/tutorial/user-driven/azure-ad-join-workflow


Theory
------

1. What is Autopilot User-Driven Mode?
   Autopilot User-Driven Mode allows end users to set up their devices with minimal IT intervention. 
   After turning on the device and signing in, the device automatically joins the organization, enrolls in Intune, and applies company policies.

2. When to Use It:

   * Device is delivered directly to end users
   * No IT/OEM/reseller interaction required
   * Designed for single-user devices
   * Works on physical devices and VMs (TPM attestation not required)

Deployment
----------

Step 1: Set up Windows automatic Intune enrollment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Sign in to Microsoft Entra ID
2. Search and access **Mobility (MDM and WIP)**
3. Select **Microsoft Intune**
4. Set the following:
   * MDM user scope: **All**
   * WIP user scope: **None**
5. Click **Save**

Step 2: Allow users to join devices to Microsoft Entra ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Sign in to Entra ID
2. Navigate to **Identity > Devices**
3. Under **Device Settings** > **Users may join devices to Microsoft Entra**: set to **All**
4. Click **Save**

Step 3: Create Dynamic Device Group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Go to Intune Admin Center > **Groups > All groups**
2. Click **New group**
3. Fill out:
   * Group type: **Security**
   * Name: `All Autopilot Device`
   * Membership type: **Dynamic Device**
4. In **Dynamic membership rules**, paste:

   ::

     (device.devicePhysicalIDs -any (_ -startsWith "[ZTDid]"))

5. Save and Create

Step 4: Configure & Assign Enrollment Status Page (ESP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ESP allows partial installs during provisioning. Recommended setting:

* Enable **"only fail selected blocking apps in technician phase"**
* Install all apps even if not blocking

A. Upload Package App (e.g. Zoom)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download Zoom MSI installer
2. Go to Intune Admin Center > **Apps > Windows > Create app**
3. Choose **Line-of-business app**
4. Upload MSI
5. Set:
   * Name: `Zoom`
   * Command-line: `/qn`
6. Assign to `All Autopilot Device` group

B. Create ESP Profile
~~~~~~~~~~~~~~~~~~~~~

1. Navigate to **Devices > Windows > Enrollment > Enrollment Status Page**
2. Click **Create** > Set:
   * Name: `ESP - Autopilot User-Driven Mode`
   * Show progress: Yes
   * Error timeout: 60 min
   * Error message: `Installation exceeded time limit...`
   * Block device use: Yes
   * Add Zoom to blocking apps
   * Assignment: `All Autopilot Device`

Step 5: Create and Assign Windows Autopilot Profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Navigate to **Devices > Windows > Enrollment > Deployment Profiles**
2. Create new profile:
   * Name: `DeployProfile - Autopilot User-Driven Mode`
   * Deployment mode: **User-driven**
   * Join to: **Microsoft Entra joined**
   * Hide license/privacy/options
   * User type: **Administrator**
   * Apply device name template: `UserDr-%SERIAL%`
   * Assign to: `All Autopilot Device`

Admin Workflow
--------------

* Register devices for Windows Autopilot
* Ensure profile is assigned in Intune

Note: Registered ≠ Enrolled in Intune

User Workflow
-------------

1. Deploy the device (trigger Autopilot enrollment)
2. Follow the OOBE flow as defined

Reference:
https://learn.microsoft.com/en-us/autopilot/tutorial/user-driven/azure-ad-join-deploy-device
