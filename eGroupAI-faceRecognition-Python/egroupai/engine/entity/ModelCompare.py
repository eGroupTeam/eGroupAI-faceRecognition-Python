import logging

class ModelCompare:
  def __init__(self) -> None:
    self.threshold=None
    self.modelFaceDBPathA=None
    self.modelFaceDBPathB=None
    self.outputCsvPath=None
    self.cli=None
    self.commandList=None
    self.disk=None
    self.enginePath=None

  def getThreshold(self):
      return self.threshold        

  def setThreshold(self,threshold):
      self.threshold=threshold     


  def getModelFaceDBPathA(self):
      return self.modelFaceDBPathA

  def setModelFaceDBPathA(self,modelFaceDBPathA):
      self.modelFaceDBPathA=modelFaceDBPathA     


  def getModelFaceDBPathB(self):
      return self.modelFaceDBPathB

  def setModelFaceDBPathB(self,modelFaceDBPathB):
      self.modelFaceDBPathB=modelFaceDBPathB


  def getOutputCsvPath(self):
      return self.outputCsvPath

  def setOutputCsvPath(self,outputCsvPath):
      self.outputCsvPath=outputCsvPath


  def getCli(self):
      return self.cli

  def setCli(self,cli):
      self.cli=cli


  def getCommandList(self):
      return self.commandList

  def setCommandList(self,commandList):
      self.commandList=commandList


  def getEnginePath(self):
      return self.enginePath

  def setEnginePath(self,enginePath):
      self.enginePath=enginePath


public class ModelCompare {
  private static Logger LOGGER = LoggerFactory.getLogger(CmdUtil.class);

  private Double threshold;
  private String modelFaceDBPathA;
  private String modelFaceDBPathB;
  private String outputCsvPath;
  private StringBuilder cli;
  private List<String> commandList;
  private String disk;
  private String enginePath;
  // init func
  private AttributeCheck attributeCheck;

  public Double getThreshold() {
    return threshold;
  }

  public void setThreshold(Double threshold) {
    this.threshold = threshold;
  }

  public String getModelFaceDBPathA() {
    return modelFaceDBPathA;
  }

  public void setModelFaceDBPathA(String modelFaceDBPathA) {
    this.modelFaceDBPathA = modelFaceDBPathA;
  }

  public String getModelFaceDBPathB() {
    return modelFaceDBPathB;
  }

  public void setModelFaceDBPathB(String modelFaceDBPathB) {
    this.modelFaceDBPathB = modelFaceDBPathB;
  }

  public StringBuilder getCli() {
    return cli;
  }

  public void setCli(StringBuilder cli) {
    this.cli = cli;
  }

  public String getEnginePath() {
    return enginePath;
  }

  public void setEnginePath(String enginePath) {
    this.enginePath = enginePath;
  }

  public List<String> getCommandList() {
    if (attributeCheck == null) {
      attributeCheck = new AttributeCheck();
    }
    if (attributeCheck.stringsNotNull(cli.toString())) {
      commandList = new ArrayList<String>();
      commandList.add("cmd");
      commandList.add("/C");
      commandList.add(disk + ": && " + cli.toString().replace("/", "/"));
    }
    return commandList;
  }

  public void setCommandList(List<String> commandList) {
    this.commandList = commandList;
  }

  public String getOutputCsvPath() {
    return outputCsvPath;
  }

  public void setOutputCsvPath(String outputCsvPath) {
    this.outputCsvPath = outputCsvPath;
  }

  public void generateCli() {
    if (attributeCheck == null) {
      attributeCheck = new AttributeCheck();
    }
    this.disk = enginePath.substring(0, 1);
    if (attributeCheck.stringsNotNull(enginePath, disk)) {
      cli = new StringBuilder("cd " + enginePath + " && " + disk + ": && ModelCompare " + threshold + " " + " \"" + modelFaceDBPathA + "\" \""
          + modelFaceDBPathB + "\" \"" + outputCsvPath + "\"");
    } else {
      cli = null;
    }
    LOGGER.info("RecognizeFace cli : " + cli);
  }
}
