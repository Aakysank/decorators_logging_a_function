from hwx import simlab

def decorator(fnPtr):
    def timeLogWrapper(fileNameWithPath :str):
        
        with open('logfile.txt', 'w') as log:
            log.write('Import of file begins\n')

        time = simlab.Timer()
        i = fnPtr(fileNameWithPath)
        ElapsedTime = time.get_lapse_time()
        with open('logfile.txt', 'a') as log:
            log.write('Import of file ends\n')
            log.write(f'Time taken for file import: {ElapsedTime}\n')
            
        return i
    return timeLogWrapper

@decorator
def ImportSTLFile(fileNameWithPath):
    ImportSTL=f''' <ImportSTL CheckBox="ON" UUID="adb3e8b0-d598-4b36-85c0-9e0e59032c66" gda="">
      <tag Value="1"/>
      <FileName Value="{fileNameWithPath}" HelpStr="File name to be imported." widget="LineEdit"/>
      <LargeFile Value="0"/>
      <SplitFaces Value="0"/>
      <RemoveTinyFaces Value="0"/>
      <MeshSize Value="2 mm"/>
      <FeatureAngle Value="0"/>
      <Output widget="NULL"/>
     </ImportSTL>''';
    simlab.execute(ImportSTL);



ImportSTLFile("D:\\Python_Practice\\decorators\\Full_Assembly_Surron_23 v2.stl")
