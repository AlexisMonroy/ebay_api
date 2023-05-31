x = 3
y = '<pic_call>'
z = 'alexis'
q = '.jpg</pic_call>'
s = ''

for i in range(x):
    pic = y + z + str(i) + q
    s = s + pic
    print(pic)
print(s)    

<ShippingDetails>
    <CalculateShippingRate>
        <OriginatingPostalCode>90260</OriginatingPostalCode>
    </CalculateShippingRate>    
</ShippingDetails>
<ShippingPackageDetails>
    <MeasurementUnit>English</MeasurementUnit>
    <PackageDepth unit="inches" measurementSystem="English">1</PackageDepth>
    <PackageLength unit="inches" measurementSystem="English">1</PackageLength>
    <PackageWidth unit="inches" measurementSystem="English">1</PackageWidth>
    <ShippingPackage>PackageThickEnvelope</ShippingPackage>
    <WeightMajor unit="lbs" measurementSystem="English">1</WeightMajor>
    <WeightMinor unit="oz" measurementSystem="English">1</WeightMinor>
</ShippingPackageDetails>