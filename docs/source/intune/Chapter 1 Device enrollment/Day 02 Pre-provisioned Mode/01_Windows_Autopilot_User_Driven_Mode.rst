Day 2-1 Pre-provisioned Mode
===================
I. Theory
---------

- **1/ What is autopilot user-driven mode**
    
    **Autopilot User-Driven Mode** lets end users set up their devices themselves with minimal IT involvement. After turning on the device and signing in, the device automatically joins the organization, enrolls in Intune, and applies company policies — ready for use.
    
- **2/ When do we use user-driven mode**
    - The Device will be **delivered directly to the end users** without IT intervention
        - Requires no interaction from IT team/OEM/reseller.
    - The device will be used primarily by **a single user**
    - Doesn't require [**TPM attestation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/tpm-key-attestation)** so works on physical devices and VMs.
        - Because user-driven does not require TPM so we can leverage this mode to test enrollment status or creating VMs for testing an autopilot process

II. Deployment
----------------

- **Step 1: Set up Windows automatic Intune enrollment**
    
    1/ Sign in to the [EntraID](https://entra.microsoft.com)
    
    .. image:: imgs/step1.png
        :alt: Demo Image
        :width: 600px
        :align: center
    
    2/ In the **EntraID** screen > search the keyword **MDM and WIP** > click on **MDM and WIP**
    
    .. image:: imgs/step1.png
        :width: 400
        :alt: Alternative text
        :align: center
    
    3/ In **Mobility (MDM and WIP)** > ****choose **Microsoft Intune**
    
    ![image.png](attachment:fccc27e1-ebf2-425d-ac31-536556ffea4f:image.png)
    
    4/ In Microsoft Intune
    
    4.1/ MDM user scope
    
    - check **All**
    
    ![image.png](attachment:a6b66d65-6af0-4b36-b652-199989bbb0ac:image.png)
    
    4.2/ Windows Information Protection(WIP) user scope
    
    - Check **None**
    
    ![image.png](attachment:3ab8e1ba-43cb-432f-8caf-1163befdc01a:image.png)
    
    5/ After setting like the picture above **select** > **Save**
    
- **Step 2: Allow users to join devices to Microsoft Entra ID**
    
    1/ Sign in to the [**Microsoft Entra ID**.](https://entra.microsoft.com)
    
    ![image.png](attachment:0782b1e8-5a15-4302-a938-505d00e97665:image.png)
    
    2/ In the **EntraID** screen, under **Identity** in the left hand pane, select **Devices**.
    
    ![image.png](attachment:36fab7ed-aa6b-4cb5-8ecd-66e119ac7bdb:image.png)
    
    3/ In the **Devices | Overview** screen, under **Manage** in the left hand pane, select **Device Settings**. 
    
    ![image.png](attachment:3945ea5f-7c54-4333-99fb-0ef40a8631e3:image.png)
    
    4/ In the **Devices | Device settings** screen that opens, under **Users may join devices to Microsoft Entra**, select **All**
    
    ![image.png](attachment:21b2458d-ae00-4537-b671-6ba676f99ae8:image.png)
    
    5/ Save
    
- **Step 3: Create a device group**
    
    Create a dynamic device group for use with Windows Autopilot
    
    1/ Sign into the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
    
    ![image.png](attachment:f2d154f3-82b7-421e-8ba4-c007cb30e16c:image.png)
    
    2/ In the Intune Admin Portal > select **Groups > All groups**
    
    ![image.png](attachment:b40513da-fcd6-4569-afc9-d62cb5094602:image.png)
    
    3/ In the **Groups | Overview** screen > make sure **All groups** is selected, and then select **New group**. 
    
    ![image.png](attachment:65e64474-f693-4486-a6be-69b7f4649ec3:image.png)
    
    3/ In the **New Group** screen that opens:
    
    - For **Group type**, select **Security**.
    - For **Group name**, enter a name for the device group [**All Autopilot Device**]
    - For **Group description > skip**
    - For **Microsoft Entra roles can be assigned to the group**, select **No**.
    - For **Membership type**, select **Dynamic Device**.
    - For **Owners >** **skip**
    - For **Dynamic device members**, select **Add dynamic query**. The **Dynamic membership rules** screen opens.
    
    ![image.png](attachment:32d772a7-0404-4316-9e56-d244e5cc6254:image.png)
    
    4/ In the **Dynamic membership rules** screen
    
    4.1/ at the Rule syntax box > select edit at the top-right hand side
    
    ![image.png](attachment:e7c16192-762f-4f22-90c8-7456690db052:image.png)
    
    4.2/ Paste in the following rule in the **Edit rule syntax** screen under **Rule syntax**
    
    `(device.devicePhysicalIDs -any (_ -startsWith "[ZTDid]"))`
    
    ![image.png](attachment:75595389-3f74-4ae2-9de1-4869577c2a4b:image.png)
    
    4.3/ Once the rule is pasted in, select **OK**.
    
    4.4/ Once the desired rule is entered, select **Save** on the toolbar to close the **Dynamic membership rules** window.
    
    ![image.png](attachment:ffa2fe6e-e6d3-4b25-aeda-3341d5f1f2b1:image.png)
    
    5/ Select **Create** to finish creating the dynamic device group.
    
    ![image.png](attachment:0bb5c6fb-d337-47c9-9397-ae8492020a69:image.png)
    
    6/ Wait until the notification is successful
    
    ![image.png](attachment:eb0ca056-4445-4392-b178-46bfe9c28154:image.png)
    
- **Step 4: Configure and assign Windows Autopilot Enrollment Status Page (ESP)**
    - ***What is ESP***
        
        ESP is often configured to wait for only specific apps (instead of all), so users can get to the desktop faster. But then pre-provisioning "completes" after those apps are installed. It will continue installing apps until reseal is pressed though. The new option [***only fail selected blocking apps in technician phase***] allows both scenarios - fast user ESP, but all apps installed in preprov ESP. 
        
        **Note that**
        
        There is a cool feature in the preprovisoning process. In the ESP setting, you can now select the "***only fail selected blocking apps in technician phase***" to YES. If you do so, during the preprovisoning phase, Windows will try to install **ALL required software**, not only the ESP blocking one, allowing you to fully prepare your devices. Works good so far for our company. 
        
    - **A. Upload A Package App**
        
        1/ Visit the link here: [Zoom Installers](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060407)
        
        2/ Download Zoom workspace desktop app for Meeting (64bit)- MSI Installer
        Or using the link here: https://zoom.us/client/latest/ZoomInstallerFull.msi?archType=x64
        
        ![image.png](attachment:3107293e-b4ad-46af-9b32-bfb5a9f6d2e1:image.png)
        
        3/ Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
        
        2/ Select **Apps** > **Apps | Overview** > **Windows**.
        
        ![image.png](attachment:437294e0-ba1d-4f73-86b3-1d3aa9f94ffc:image.png)
        
        3/ In **Windows | Windows Apps** > select **Create**
        
        ![image.png](attachment:05b75231-adfd-4e12-a0ca-9e4c19e9c783:image.png)
        
        4/ In the **Select app type** pane, under the **Other** app types, select **Line-of-business app**. 
        
        ![image.png](attachment:db5460be-7c47-43ec-b1b9-f56d25202502:image.png)
        
        4/ Select **Select**. The **Add app** steps are displayed.
        
        ![image.png](attachment:fa977888-e880-4d5b-afdf-b7d94d5d13df:image.png)
        
        5/ In the **Add app** pane, select **Select app package file**.
        
        ![image.png](attachment:4f14a409-1c83-4eb7-af82-e635e00cf410:image.png)
        
        6/ **Upload** the **ZoomMSI** file downloaded recently, select **OK**
        
        ![image.png](attachment:a5e9070f-1e2a-4c71-b424-69179cd6edd9:image.png)
        
        7/ In App information > select **Next**
        
        - Name: **Zoom**
        - Description: **skip**
        - Publisher: **Zoom**
        - App install context: **Device**
        - Ignore app version: **No**
        - Command-line arguments: `/qn`
        - Upload Logo
        - The other fields: **skip**
        
        ![image.png](attachment:b457ec6c-e4ae-46ee-af55-8213f2b0067a:image.png)
        
        ![image.png](attachment:5c917d04-f450-405f-b6c0-3c8211fffd18:image.png)
        
        8/ At the **scope tags** screen > select Next
        
        ![image.png](attachment:49146881-d399-4442-a360-0dd9486ff283:image.png)
        
        9/ At the Assignments screen > Assign to the desired group > select Next
        
        9.1/ At the **Required header** > select **add group**
        
        ![image.png](attachment:1067edb0-abff-438e-ae01-99dc18be8b34:image.png)
        
        9.2/ Enter [**All Autopilot Device**] > Check **box** > click **Select**
        
        ![image.png](attachment:1b5fab24-283b-4bc1-a69e-dfec70876337:image.png)
        
        9.3/ Ensure the target group is there > select **Next**
        
        ![image.png](attachment:5180ebe4-2317-46ae-8337-9c74176345a1:image.png)
        
        10/ At the review + Create tab > select create
        
        ![image.png](attachment:e70f240b-37e5-4d72-9f45-593f467757a4:image.png)
        
        11/ Wait until the uploading zoom is completed
        
        ![image.png](attachment:dc3f89e5-9c57-44ff-af4d-3a4f65bd92ed:image.png)
        
        12/ uploading process is successful
        
        ![image.png](attachment:7e2c7e41-d0fd-45a6-8bdd-6a40f67836cd:image.png)
        
    - **B. Create ESP Profile**
        
        1/ Sign into the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
        
        2/ In the **Home** screen, select **Devices** in the left hand pane.
        
        ![image.png](attachment:c65ba2e1-2ec4-402c-908d-75af4bad3c7b:image.png)
        
        3/ In the **Devices | Overview** screen, under **Manage devices by platform**, select **Windows**.
        
        ![image.png](attachment:79af17c4-e0a8-4aff-a508-e8eb7d4edb11:image.png)
        
        4/ In the **Windows | Windows devices** screen, under **Device onboarding**, select **Enrollment** at the left pane side.
        
        ![image.png](attachment:58af8fdb-6151-45a0-859b-741992291580:image.png)
        
        5/ In the **Windows | Windows enrollment** screen, under **Windows Autopilot**, select **Enrollment Status Page**.
        
        ![image.png](attachment:0f955410-893a-4c87-bfab-98ffa4898b8b:image.png)
        
        6/ In the **Enrollment Status Page** screen that opens, select **Create**.
        
        ![image.png](attachment:3d56c87e-bc71-4974-9f56-aeb576b699e8:image.png)
        
        7/ The **Create profile** screen opens. In the **Basics** page:
        
        - Next to **Name**, enter [ESP - Autopilot User-Driven Mode]
        - Next to **Description**, **skip**
        - Select **Next**.
        
        ![image.png](attachment:569610d4-9dec-4436-bea6-e55a50d14313:image.png)
        
        8/ In the **Settings** page, toggle the option **Show app and profile configuration progress** to **Yes**.
        
        ![image.png](attachment:4d5b9d19-24ce-479f-856b-ccb18ed8b8a1:image.png)
        
        8.1/ After toggling the setting to Yes > configure these settings following
        
        - Show an error when installation takes longer than specified number of minutes: **60**
        - Show custom message when time limit or error occurs: **Yes**
        - in the box message: *[Installation exceeded the time limitation set by your organization. Please try again or contact your IT support person for help]*
            
            ![image.png](attachment:df4ed820-5801-4e5d-af83-422b59ed18ad:image.png)
            
        
        8.2/ After entering the message > turn on these settings below
        
        - Turn on log collection and diagnostics page for end users: **Yes**
        - Only show page to devices provisioned by out-of-box experience (OOBE): **Yes**
        - Block device use until all apps and profiles are installed: **Yes**
        - Allow users to reset device if installation error occurs: **Yes**
        - Block device use until required apps are installed if they are assigned to the user/device: Selected
            
            ![image.png](attachment:133ae393-576c-4c88-8563-2b4197a48c29:image.png)
            
        
        8.2/ After choosing [**selected**] mode > click on **+select apps**
        
        ![image.png](attachment:d274d1da-94b5-4e73-836f-17ea2208e99f:image.png)
        
        8.3/ At the **Select apps** > search **Zoom** > Click on Zoom and **select**
        
        ![image.png](attachment:fd3072ac-dcaf-499b-8341-3dff3dab92ac:image.png)
        
        8.3/ Ensure **Zoom** is listed in the **Blocking apps** list > select **Next**
        
        ![image.png](attachment:c4056650-ac11-4a3b-b72e-9ee7d37f6508:image.png)
        
        8.4/ After adding Zoom, at [Only fail selected blocking apps in technician phase] > Select **No >** then select **Next**
        
        ![image.png](attachment:185d25b0-374b-40cc-b515-82efc509d174:image.png)
        
        9/ at **Assignment** tab > click **add groups**
        
        ![image.png](attachment:d4f14b29-5567-4388-ab05-233a3ed81129:image.png)
        
        9.1/ At the select groups to include
        
        - Search [**All autopilot device**]
        - **Check** **box** and click **Select**
        
        ![image.png](attachment:70779a6f-7b42-4ddc-8435-d6dceb8da1c9:image.png)
        
        10/ Ensure the target group is listed in the list > select **Next**
        
        ![image.png](attachment:3e390332-1a83-4663-ab04-bb93c808e9d4:image.png)
        
        11/ At the scope tags > select **Next**
        
        ![image.png](attachment:bccf63c0-0a81-4368-889f-8ac0ad4b5b5b:image.png)
        
        12/ At the **Review and create** tab > select **Create**
        
        ![image.png](attachment:5d438b72-e042-4f49-9c54-c25e040cc0d0:image.png)
        
        13/ Waiting until the notifications shows **[profile successfully created /assigned]**
        
        ![image.png](attachment:0c722068-0e19-4f6b-8493-dd59a7acf4d3:image.png)
        
- **Step 5: Create and assign Windows Autopilot profile**
    1. Sign into the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
    2. In the **Home** screen, select **Devices** in the left hand pane.
        
        ![image.png](attachment:54c193b7-b4f9-440d-881f-ebf03bb5c355:image.png)
        
    3. In the **Devices | Overview** screen, under **By platform**, select **Windows**.
        
        ![image.png](attachment:8a3287bf-f790-47af-91de-49a91d3ca5de:image.png)
        
    4. In the **Windows | Windows devices** screen, under **Device onboarding**, select **Enrollment**.
        
        ![image.png](attachment:479b7805-c4ee-4a28-b554-75b3a374716f:image.png)
        
    5. In the **Windows | Windows enrollment** screen, under **Windows Autopilot**, select **Deployment Profiles**.
        
        ![image.png](attachment:0192dac5-4d36-4e09-aa58-cc4b0125bb11:image.png)
        
    6. In the **Windows Autopilot deployment profiles** screen, select the **Create Profile** drop down menu and then select **Windows PC**.
        
        ![image.png](attachment:027e7579-ec31-4e53-abfa-527983361e5f:image.png)
        
    7. The **Create profile** screen opens. In the **Basics** page:
        1. Next to **Name: [DeployProfile** - Autopilot User-Driven Mode**]**
        2. Next to **Description**
        3. **Next**.
        
        ![image.png](attachment:5d20a804-6118-4f0d-b578-b19628b502bb:image.png)
        
    
    8.1. In the **Out-of-box experience (OOBE)** page:
    
    - For **Deployment mode**, select **User-driven**.
    - For **Join to Microsoft Entra ID as**, select **Microsoft Entra joined**.
    - For **Microsoft Software License Terms**, select **Hide**
    - For **Privacy settings**, select **Hide**
        
        ![image.png](attachment:2385d8d5-238c-44a6-aff3-27874364362c:image.png)
        
    
    8.2. In the **Out-of-box experience (OOBE)** page:
    
    - For **Hide change account options**, select **Hide**.
    - For **User account type**, select **Administrator**.
    - For **Allow pre-provisioned deployment**, select **No**.
    - For **Language (Region): Skip**
    - For **Automatically configure keyboard:  No**
    - For **Apply device name template: UserDr-%SERIAL%**
    - Next
        
        ![image.png](attachment:5f70bdf6-214e-408d-a8a8-c48ba11651ed:image.png)
        
    1. In the **Scope Tags** tab > **Next**
        
        ![image.png](attachment:ec1f96d1-ff7b-458a-8bd8-11e6a2b216f8:image.png)
        
    2. In the **Assignments** tab 
        - Under **Included groups**, select **Add groups**.
        
        ![image.png](attachment:6ef7392f-c499-4a1f-b9d4-53c8f86f329e:image.png)
        
        - select the group that created in the **Step 3 [All Autopilot Device]**
        
        ![image.png](attachment:a9c2ac5a-a894-43c4-9e83-d043a11b7535:image.png)
        
        - Next
    3. In the **Assignments** > **Create**
        
        ![image.png](attachment:b0691435-6f1c-49f9-b7f2-1d1aa474aa63:image.png)
        
    4. Wait until the notification is successful 
        
        ![image.png](attachment:0613e95d-7751-434e-9f07-8728fe289b49:image.png)
        

III.  Admin Workflow
-----------------------

Before a device can use Windows Autopilot, the device must be registered as a Windows Autopilot device.

Registering a device as a Windows Autopilot device makes the Windows Autopilot service available to the device.

Note that

- a device isn't currently enrolled Intune
- a device registered in Windows Autopilot doesn't mean the device is enrolled in Intune.
- **Step 1: Register devices as Windows Autopilot devices**
    
    https://learn.microsoft.com/en-us/autopilot/troubleshooting-faq#why-is-the-join-type-for-a-device-showing-as--microsoft-entra-registered--instead-of--microsoft-entra-joined--
    
- **Step 2: Verify device has a Windows Autopilot profile assigned to it**

IV. User Workflow
--------------------

Registering a device as a Windows Autopilot device doesn't mean that the device has used the Windows Autopilot service. It just makes the Windows Autopilot service available to the device.

- **Step 1: [Deploy the device](https://learn.microsoft.com/en-us/autopilot/tutorial/user-driven/azure-ad-join-deploy-device)**