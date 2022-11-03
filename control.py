from androidhelper import Android as _android
import time as _time

_droid = _android()

def getMainAndroid():return _droid

class Clipboard():
    def getClipboard():
        return _droid.getClipboard().result

    def setClipboard(c):
        _droid.setClipboard(c)

class Vibrator():
    def vibrate(t = None):
        if t==None:
            _droid.vibrate()
        else:
            _droid.vibrate(t)

class Network():
    def getStatus():
        return _droid.getNetworkStatus().result

class Toast():
    def makeToast(msg):
        _droid.makeToast(msg)

class Notification():
    def makeNotification(title, message, url = None):
        if url==None:
            _droid.notify(title, message)
        else:
            _droid.notify(title, message, url)

class Applications():
    def getLaunchableApplications():
        return _droid.getLaunchableApplications().result
    
    def launch(c):
        _droid.launch(c)
    
    def getRunningPackages():
        return _droid.getRunningPackages().result
    
    def forceStopPackage(n):
        _droid.forceStopPackage(n)

class Camera():
    def capturePicture(path):
        return _droid.cameraCapturePicture(path).result
    
    def interactiveCapturePicture(path):
        return _droid.cameraInteractiveCapturePicture(path)

class BarCode():
    def scan():
        return _droid.scanBarcode().result
    
class Contacts():
    def pick():
        return _droid.pickContact().result
    
    def pickPhone():
        return _droid.pickPhone().result
    
    def getAttributes():
        return _droid.contactGetAttributes().result
    
    def getIds():
        return _droid.contactsGetIds().result
    
    def get(attr):
        return _droid.contactsGet(attr).result
    
    def getById(id):
        return _droid.contactsGetById(id).result
     
    def getCount():
        return _droid.contactsGetCount().result
    
class Location():
    def providers():
        return _droid.locationProviders().result
    
    def providerStatus(pro):
        return _droid.locationProviderEnabled(pro).result
    
    def start(dis, udis):
        _droid.startLocating(dis, udis)
    
    def read():
        return _droid.readLocation().result
       
    def getLastKnown():
        return _droid.getLastKnownLocation().result
        
    def geocode(lat, lon, maxlen):
        return _droid.geocode(lat, lon, maxlen)
    
    def stop():
        _droid.stopLocating()

class Phone():
    def startTrackingState():
        _droid.startTrackingPhoneState()
    
    def stopTrackingState():
        _droid.stopTrackingPhoneState()
    
    def state():
        return _droid.readPhoneState().result
    
    def call(uri):
        _droid.phoneCall(uri)
    
    def callNumber(num):
        _droid.phoneCallNumber(num)
    
    def dial(uri):
        _droid.phoneDial(uri)
    
    def dialNumber(num):
        _droid.phoneDialNumber(num)
    
    def cellLocation():
        return _droid.getCellLocation().result
    
    def networkOperator():
        return _droid.getNetworkOperator().result
    
    def networkOperatorName():
        return _droid.getNetworkOperatorName().result
    
    def networkType():
        return _droid.getNetworkType().result
    
    def type():
        return _droid.getPhoneType().result
    
    class Sim():
        def countryISO():
            return _droid.getSimCountryIso().result
    
        def operator():
            return _droid.getSimOperator().result
    
        def serialNumber():
            return _droid.getSimSerialNumber().result
     
        def operator():
            return _droid.getSimOperator().result
        
        def operatorName():
            return _droid.getSimOperatorName().result
        
        def serialNumber():
            return _droid.getSimSerialNumber().result
        
        def state():
            return _droid.getSimState().result
    
    def subscriberId():
        return _droid.getSubscriberId().result
    
    def voiceMailAlphaTag():
        return _droid.getVoiceMailAlphaTag().result
    
    def voiceMailNumber():
        return _droid.getVoiceMailNumber().result
    
    def checkNetworkRoaming():
        return _droid.checkNetworkRoaming().result
    
    def deviceId():
        return _droid.getDeviceId().result
    
    def deviceSoftwareVersion():
        return _droid.getDeviceSoftwareVersion().result
    
    def line1Number():
        return _droid.getLine1Number().result
    
    def neighboringCellInfo():
        return _droid.getNeightboringCellInfo().result
    
class Recorder():
    SIZE_160x120 = 0
    SIZE_320x240 = 1
    SIZE_352x288 = 2
    SIZE_640x480 = 3
    SIZE_800x480 = 4
    
    def startMicrophone(path):
        _droid.recorderStartMicrophone(path)
    
    def startVideo(path, dura, videoSize):
        _droid.recorderStartVideo(path, dura, videoSize)
        
    def captureVideo(path, dura, micro):
        _droid.recorderCaptureVideo(path, dura, micro)
    
    def startInteractiveVideoRecording(path):
        _droid.startInteractiveVideoRecording(path)
     
    def stop():
        _droid.recorderStop()

class Sensors():
    def startTimed(sensor, delay):
        _droid.startSensingTimed(sensor, delay)
    
    def startThreshold(sensor, threshold, axis):
        _droid.startSensingThreshold(sensor,thresholf, axis)
    
    def startSensing(sampleSize):
        _droid.startSensing(sampleSize)
    
    def stopSensing():
        _droid.stopSensing()
    
    def read():
        return _droid.readSensors().result
    
    def accuracy():
        return _droid.sensorsGetAccuracy().result
    
    def light():
        return _droid.sensorsGetLight().result
    
    def accelerometer():
        return _droid.sensorsReadAccelerometer().result
    
    def magnetometer():
        return _droid.sensorsReadMagnetometer().result
    
    def orientation():
        return _droid.sensorsReadOrientation().result
    
class Settings():
    def screenTimeout():
        return _droid.getScreenTimeout().result
    
    def setScreenTimeout(time):
        _droid.setScreenTimeout(time)
    
    def airplaneMode():
        return _droid.checkAirplainMode().result
    
    def setAirplaneMode(on):
        _droid.toggleAirplane(on)
    
    def ringerSilentMode():
        return _droid.checkRingerSilentMode().result
    
    def setRingerSilentMode(on):
        _droid.toggleRingerSilentMode(on)
        
    def vibrateMode(ringer):
        return _droid.getVibrateMode(ringer).result
    
    def setVibrateMode(on):
        _droid.toggleVibrateMode(on)
    
    class RingerVolume():
        def level():
            return _droid.getRingerVolume().result/_droid.getMaxRingerVolume().result*100
        
        def setLevel(volume):
            _droid.setRingerVolume(volume/100*_droid.getMaxRingerVolume().result)

    class MediaVolume():
        def level():
            return _droid.getMediaVolume().result/_droid.getMaxMediaVolume().result*100
        
        def setLevel(volume):
            _droid.setMediaVolume(volume/100*_droid.getMaxMediaVolume().result)
    
    def screenBrightness():
        return _droid.getScreenBrightness().result
    
    def setScreenBrightness(brightness):
        _droid.setScreenBrightness(brightness)
    
    def screenOn():
        return _droid.checkScreenOn().result

class Sms():
    def send(addr, text):
        _droid.smsSend(addr, text)
    
    def messageCount(unreadonly, folder = 'inbox'):
        return _droid.smsGetMessageCount(unreadonly, folder).result
    
    def messageIds(unreadonly, folder = 'inbox'):
        return _droid.smsGetMessageIds(unreadonly, folder).result
    
    def messages(unreadonly, attributes = None, folder = 'inbox'):
        if attributes==None:
            return _droid.smsGetMessages(unreadonly, folder).result
        else:
            return _droid.smsGetMessages(unreadonly, folder, attributes).result
    
    def message(id, attributes = None):
        if attributes==None:
            return _droid.smsGetMessageById(id)
        else:
            return _droid.smsGetMessageById(id, attributes)
    
    def attributesList():
        return _droid.smsGetAttributes().result
    
    def deleteMessage(id):
        return _droid.smsDeleteMessage(id).result
    
    def markMessages(ids, read):
        return _droid.smsMarkMessageRead(ids, read).result
    
class SpeechRecognition():
    def recognize():
        return _droid.recognizeSpeech().result

class DtmfTonesGenerator():
    def generate(phoneNumber, duration = 100):
        _droid.generateDtmfTones(phoneNumber, duration)

class WakeLock():
    def acquireFull():
        _droid.wakeLockAcquireFull()

    def acquirePartial():
        _droid.wakeLockAcquirePartial()

    def acquireBright():
        _droid.wakeLockAcquireBright()

    def acquireDim():
        _droid.wakeLockAcquireDim()
    
    def release():
        _droid.wakeLockRelease()

class Wifi():
    def scan():
        return _droid.wifiStartScan().result
    
    def scanResult():
        return _droid.wifiGetScanResults().result
    
    class WifiLock():
        def acquireFull():
            _droid.wifiLockAcquireFull()
        
        def acquireScanOnly():
            _droid.wifiLockAcquireScanOnly()
        
        def release():
            _droid.wifiLockRelease()
    
    def active(on = None):
        if on==None:
            return _droid.checkWifiState().result
        else:
            _droid.toggleWifiState(on)
    
    def disconnect():
        return _droid.wifiDisconnect().result
    
    def connection():
        return _droid.getConnectionInfo().result
    
    def reassociate():
        return _droid.wifiReassociate().result
    
    def reconnect():
        return _droid.wifiReconnect().result
    
class Battery():
    STATUS_UNKNOWN = 1
    STATUS_CHARGING = 2
    STATUS_DISCHARGING = 3
    STATUS_NOTCHARGING = 4
    STATUS_FULL = 5
    
    HEALTH_UNKNOW = 1
    HEALTH_GOOD = 2
    HEALTH_OVERHEAT = 3
    HEALTH_DEAD = 4
    HEALTH_OVERVOLTAGE = 5
    HEALTH_UNSPECIFIED_FAILURE = 6
    
    PLUGTYPE_UNKNOWN = -1
    PLUGTYPE_NONE = 0
    PLUGTYPE_AC = 1
    PLUGTYPE_USB = 2
    
    def data():
        return _droid.readBatteryData().result
    
    def startMonitoring():
        _droid.batteryStartMonitoring()
    
    def stopMonitoring():
        _droid.batteryStopMonitoring()
    
    def status():
        return _droid.batteryGetStatus().result
    
    def health():
        return _droid.batteryGetHealth().result
    
    def plugType():
        return _droid.batteryGetPlugType().result
    
    def present():
        return _droid.batteryCheckPresent().result
    
    def level():
        return _droid.batteryGetLevel().result
    
    def voltage():
        return _droid.batteryGetVoltage().result
    
    def temperature():
        return _droid.batteryGetTemperature().result
    
    def technology():
        return _droid.batteryGetTechnology().result
    
class Preferences():
    def value(key, filename = None):
        if filename==None:
            return _droid.prefGetValue(key).result
        return _droid.prefGetValue(key, filename).result
    
    def setValue(key, value, filename = None):
        if filename==None:
            _droid.prefPutValue(key, value)
        else:
            _droid.prefPutValue(key, value, filename)
    
    def all(filename = None):
        return _droid.prefGetAll().result

class TextToSpeach():
    def speak(text):
        _droid.ttsSpeak(text)
    
    def isSpeaking():
        return _droid.ttsIsSpeaking().result
    
    def speakAndWait():
        _droid.ttsSpeak(text)
        while _droid.ttsIsSpeaking().result:
            _time.sleep(0.01)
        
class Bluetooth():
    SMODE_BLUETOOTHOFF = -1
    SMODE_NOTUSE = 0
    SMODE_CONN = 1
    SMODE_DISCO = 2
    
    def activeConnections():
        return _droid.bluetoothActiveConnections()
    
    def writeBinary(base64, connID = None):
        if connID==None:
            _droid.bluetoothWriteBinary(base64)
        else:
            _droid.bluetoothWriteBinary(base64, connID)
    
    def readBinary(bufferSize = 4096, connID = None):
        if connID==None:
            _droid.bluetoothReadBinary(bufferSize)
        else:
            _droid.bluetoothReadBinary(bufferSize, connID)
    
    def connect(uuid, addr = None):
        if addr==None:
            return _droid.bluetoothConnect(uuid)
        else:
            return _droid.bluetoothConnect(uuid, addr)
    
    def accept(uuid, timeout=0):
        _droid.bluetoothAccept(uuid, timeout)
    
    def makeDiscoverable(duration=300):
        _droid.makeDiscoverable(time)
    
    def write(ascii, connID):
        _droid.bluetoothWrite(ascii, connID)
    
    def readRead(connID):
        return _droid.bluetoothReadReady(connID).result
    
    def read(bufferSize = 4096, connID = None):
        if connID==None:
            return _droid.bluetoothRead(bufferSize).result
        else:
            return _droid.bluetoothRead(bufferSize, connID).result
    
    def readLine(connId = None):
        if connID==None:
            return _droid.bluetoothReadLine().result
        return _droid.bluetoothReadLine(connID).result
    
    def remoteDeviceName(addr):
        return _droid.bluetoothGetRemoteDeviceName(addr).result
    
    def localName():
        return _droid.bluetoothGetLocalName().result
    
    def scanMode():
        return _droid.bluetoothGetScanMode().result
     
    def connectedDeviceName(connID):
        return _droid.bluetoothConnectedDeviceName(connID).result
    
    def active(on = None, ask = True):
        if on==None:
            return _droid.checkBluetoothState().result
        else:
            _droid.toggleBluetoothState(on, ask)
    
    def stop(connID):
        _droid.bluetoothStop(connID)
    
    def localAdress():
        return _droid.bluetoothGetLocalAdress().result
    
    def discoveryStart():
        return _droid.bluetoothDiscoveryStart().result
    
    def discoveryCancel():
        return _droid.bluetoothDiscoveryCancel().result
    
    def isDiscoverable():
        return _droid.bluetoothIsDiscovering().result
    
class SignalStrengths():
    def startTracking():
        _droid.startTrackingSignalStrengths()
    
    def read():
        return _droid.readSignalStrentghs().result
    
    def stopTracking():
        _droid.stopTrackingSignalStrengths()

class Webcam():
    def start(resol = 0, qual = 20, port = 0):
        return _droid.webcamStart(resol, qual, port).result
    
    def adjustQuality(resol = 0, qual = 20):
        return _droid.webcamAdjustQuality(resol, qual)
    
    def startPreview(path, resol = 0, qual = 20):
        return _droid.cameraStartPreview(resol, qual, path)
    
    def stopPreview():
        _droid.cameraStopPreview()
    