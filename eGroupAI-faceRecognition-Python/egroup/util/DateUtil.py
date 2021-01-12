import datetime
import calendar


class Formate:
	YMDTHMSZ_="yyyy-MM-dd'T'HH:mm:ssZ"
	YMDTHMS_="yyyy-MM-dd'T'HH:mm:ss"
	YMDHMS_="yyyy-MM-ddHH:mm:ss"
	YMD_SPACE_HMS_="yyyy-MM-dd HH:mm:ss"
	YMD_SPACE_H_="yyyy-MM-dd HH"
	YMD_SPACE_HMSS_="yyyy-MM-dd HH:mm:ss.S"
	YMD_="yyyy-MM-dd"
	YMD="yyyy/MM/dd"
	MINGUO_TEXT="yyy年MM月dd日"
	MINGUO_DIGITAL="yyy-MM-dd"

	def __init__(self,value: str) -> None:
		self.value=value
	
	def getValue(self)->str:
		return self.value

class Zone:
	TAIPEI="Asia/Taipei"

	def __init__(self,value: str) -> None:
		self.value=value
	
	def getValue(self)->str:
		return self.value

class Formula:
	PLUS="Plus"
	MINUS="Minus"

	def __init__(self,value: str) -> None:
		self.value=value
	
	def getValue(self)->str:
		return self.value

class Category:
	SECONDS="Seconds"
	HOURS="Hours"
	DAYS="Days"
	MONTHS="Months"
	YEARS="Years"

	def __init__(self,value: str) -> None:
		self.value=value
	
	def getValue(self)->str:
		return self.value

class Compare:
	BEFORE="Before"
	AFTER="After"
	EQUALS="Equals"

	def __init__(self,value: str) -> None:
		self.value=value
	
	def getValue(self)->str:
		return self.value

class Duration_:
	NANOS="Nanos"
	MILLIS="Millis"
	MINUTES="Minutes"
	HOURS="Hours"
	DAYS="Days"

	def __init__(self,value: str) -> None:
		self.value=value
	
	def getValue(self)->str:
		return self.value

class Calendar_:
	ANNO_DOMINI="AnnoDomini"
	MINGUO="Minguo"

	def __init__(self,value: str) -> None:
		self.value=value
	
	def getValue(self)->str:
		return self.value


class DateUtil:

		
	def MinguroGenerate(calender_: Calendar_,formate: Formate,Local):
		pass

	
	def getDateString(formate,calendar_):
		if calendar_.getValue()=="AnnoDomini":
			current_datetime=datetime.datetime.now(tz="Asia/Taipei")
			return datetime.date.strftime(current_datetime,formate)
			



public class DateUtil {
	

	
	public String getDateString(Formate formate,Calendar_ calendar_) {
		if(calendar_.getValue().equals("AnnoDomini")){
			final ZoneId zoneId = ZoneId.of("Asia/Taipei");
			final ZonedDateTime zonedDateTime = ZonedDateTime.now(zoneId);
			final DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			return zonedDateTime.format(formatter);
		}else{
			final LocalDateTime localDateTime = LocalDateTime.now();	
			return MinguoGenerate(calendar_ , formate, localDateTime);
		}		
	}

		private String MinguoGenerate(Calendar_ calendar_,Formate formate ,LocalDateTime localDateTime){
		final MinguoDate minguoDate = MinguoDate.from(localDateTime);
		switch (formate.getValue()) {
		case "yyy年MM月dd日":
			return minguoDate.toString().replace("Minguo ROC", "中華民國");
		case "yyy-MM-dd":
			return minguoDate.toString().replace("Minguo ROC", "中華民國").replace("-", "年").replace("-", "月")+"日";
		default:
			return null;
		}
	}
	
	
	public String getDateStringTransfer_zoneTime(Formate formateInput ,Formate formateOutput ,String dateString ,Calendar_ calendar_) {
		if(attributeCheck.stringsNotNull(dateString)){
			final DateTimeFormatter formatterInput = DateTimeFormatter.ofPattern(formateInput.getValue());
			if(calendar_.getValue().equals("AnnoDomini")){
				final DateTimeFormatter formatterOuptut = DateTimeFormatter.ofPattern(formateOutput.getValue());
				final ZonedDateTime zonedDateTime = ZonedDateTime.parse(dateString, formatterInput);
				return zonedDateTime.format(formatterOuptut);
			}else{
				final LocalDateTime localDateTime = LocalDateTime.parse(dateString,formatterInput);
				return MinguoGenerate(calendar_ , formateOutput, localDateTime);
			}
		}
		return null;
	}
	
	public String getDateStringTransfer_zoneTime_fromTimestamp(Formate formateInput,Formate formateOutput,Timestamp timestamp) {
		if(timestamp!=null){
			final DateTimeFormatter formatterInput = DateTimeFormatter.ofPattern(formateInput.getValue());
			final DateTimeFormatter formatterOuptut = DateTimeFormatter.ofPattern(formateOutput.getValue());
			final ZonedDateTime zonedDateTime = ZonedDateTime.parse(timestamp.toString(), formatterInput);
			return zonedDateTime.format(formatterOuptut);
		}
		return null;
	}
	
	public String getDateStringTransfer_zoneTime_fromTimestampAddZone(Formate formateInput,Formate formateOutput,Zone zone,Timestamp timestamp) {
		if(timestamp!=null){
			final ZoneId zoneId = ZoneId.of(zone.getValue());			
			final DateTimeFormatter formatterInput = DateTimeFormatter.ofPattern(formateInput.getValue());
			final DateTimeFormatter formatterOuptut = DateTimeFormatter.ofPattern(formateOutput.getValue());
			final LocalDateTime localDateTime = LocalDateTime.parse(timestamp.toString(), formatterInput);			
			final ZonedDateTime zonedDateTime = localDateTime.atZone(zoneId);
			return zonedDateTime.format(formatterOuptut);
		}
		return null;
	}
	
	public String getDateStringTransfer_zoneTime_fromTimestampAddZone(Formate formateInput,Formate formateOutput,Zone zone,String timestampString) {
		if(timestampString!=null){
			final ZoneId zoneId = ZoneId.of(zone.getValue());			
			final DateTimeFormatter formatterInput = DateTimeFormatter.ofPattern(formateInput.getValue());
			final DateTimeFormatter formatterOuptut = DateTimeFormatter.ofPattern(formateOutput.getValue());
			final LocalDateTime localDateTime = LocalDateTime.parse(timestampString, formatterInput);			
			final ZonedDateTime zonedDateTime = localDateTime.atZone(zoneId);
			return zonedDateTime.format(formatterOuptut);
		}
		return null;
	}
	
	public String getDateStringTransfer_localDateTime(Formate formateInput,Formate formateOutput,String dateString ,Calendar_ calendar_) {
		if(attributeCheck.stringsNotNull(dateString)){
			final DateTimeFormatter formatterInput = DateTimeFormatter.ofPattern(formateInput.getValue());
			if(calendar_.getValue().equals("AnnoDomini")){
				// System.out.println("dateString = "+dateString+",length="+dateString.length());
				if(dateString.length()<19){
					int zero_length = 19-dateString.length();
					for(int i=1;i<zero_length+1;i++){						
						if(i%2==1){
							dateString = dateString+"0";
						}else{
							dateString = dateString+":0";
						}
						
					}
				}
				// System.out.println("dateString = "+dateString+",length="+dateString.length());
				final DateTimeFormatter formatterOuptut = DateTimeFormatter.ofPattern(formateOutput.getValue());
				final LocalDateTime localDateTime = LocalDateTime.parse(dateString, formatterInput);
				return localDateTime.format(formatterOuptut);
			}else{
				final LocalDateTime localDateTime = LocalDateTime.parse(dateString,formatterInput);
				return MinguoGenerate(calendar_ , formateOutput,localDateTime);
			}
		}
		return null;
	}
	
	public String getDateStringTransfer_localDateTime_fromTimestamp(Formate formateInput,Formate formateOutput,Timestamp timestamp) {
		if(timestamp!=null){
			final DateTimeFormatter formatterInput = DateTimeFormatter.ofPattern(formateInput.getValue());
			final DateTimeFormatter formatterOuptut = DateTimeFormatter.ofPattern(formateOutput.getValue());
			final LocalDateTime localDateTime = LocalDateTime.parse(timestamp.toString(), formatterInput);
			return localDateTime.format(formatterOuptut);
		}
		return null;
	}
	
	public  boolean getDateString_compare2Date(Formate formate,String dateString1,Compare compare,String dateString2){
		boolean flag = false;
		if(attributeCheck.stringsNotNull(dateString1,dateString2)){
			final DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			final LocalDateTime localDateTime1 = LocalDateTime.parse(dateString1, formatter);
			final LocalDateTime localDateTime2 = LocalDateTime.parse(dateString2, formatter);	
			switch (compare.getValue()) {
			case "Before":
				flag = localDateTime1.isBefore(localDateTime2);
				break;
			case "After":
				flag = localDateTime1.isAfter(localDateTime2);
				break;
			case "Equals":
				flag = localDateTime1.equals(localDateTime2);
				break;
			default:
				break;
			}
		}
		return flag;
	}
	
	public boolean getDateString_nowCompareWith(Formate formate,Compare compare,String dateString){
		boolean flag = false;
		if(attributeCheck.stringsNotNull(dateString)){
			final DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			final LocalDateTime localDateTime1 = LocalDateTime.now();
			final LocalDateTime localDateTime2 = LocalDateTime.parse(dateString, formatter);
			if(compare.getValue().equals("before")){
				flag = localDateTime1.isBefore(localDateTime2);
			}else{
				flag = localDateTime1.isAfter(localDateTime2);
			}
		}
		return flag;
	}

	
	public String getDateString_calculate(String startDateString,Formate formate,Category category,Formula formula,Long digital){
		String dateString = "";
		if(attributeCheck.stringsNotNull(startDateString)){
			DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			ZonedDateTime zonedDateTime_now = ZonedDateTime.parse(startDateString, formatter);
//			System.out.println("zonedDateTime_now="+zonedDateTime_now.format(formatter));
			
			switch (category.getValue()) {
			case "Seconds":
				dateString = caculateSeconds(zonedDateTime_now, formula, formate, digital);
				break;
			case "Hours":
				dateString = caculateHours(zonedDateTime_now, formula, formate, digital);
				break;
			case "Days":
				dateString = caculateDays(zonedDateTime_now, formula, formate, digital);
				break;
			case "Months":
				dateString = caculateMonths(zonedDateTime_now, formula, formate, digital);	
				break;
			case "Years":
				dateString = caculateYears(zonedDateTime_now, formula, formate, digital);	
				break;

			default:
				break;
			}
//			System.out.println("dateString="+dateString);
		}
		return dateString;
	}

	public  String getDateString_calculate(Formate formate,Category category,Formula formula,Long digital){
		final ZoneId zoneId = ZoneId.of("Asia/Taipei");
		final ZonedDateTime zonedDateTime_now = ZonedDateTime.now(zoneId);
		final DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
//		System.out.println("zonedDateTime_now="+zonedDateTime_now.format(formatter));
		
		String dateString = "";
		switch (category.getValue()) {
		case "Seconds":
			dateString = caculateSeconds(zonedDateTime_now, formula, formate, digital);
			break;
		case "Hours":
			dateString = caculateHours(zonedDateTime_now, formula, formate, digital);
			break;
		case "Days":
			dateString = caculateDays(zonedDateTime_now, formula, formate, digital);
			break;
		case "Months":
			dateString = caculateMonths(zonedDateTime_now, formula, formate, digital);	
			break;
		case "Years":
			dateString = caculateYears(zonedDateTime_now, formula, formate, digital);	
			break;

		default:
			break;
		}
//		System.out.println("dateString="+dateString);
		return dateString;
	}
	
	private String caculateSeconds(ZonedDateTime zonedDateTime_now,Formula formula,Formate formate,Long digital) {
		if(zonedDateTime_now!=null){
			ZonedDateTime zonedDateTime_result =null;
			switch (formula.getValue()) {
			case "Plus":
				zonedDateTime_result = zonedDateTime_now.plusSeconds(digital);		
				break;
			case "Minus":
				zonedDateTime_result = zonedDateTime_now.minusSeconds(digital);				
				break;
			default:
				break;
			}
			final  DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			return zonedDateTime_result.format(formatter);
		}
		return null;
	}
	
	private String caculateHours(ZonedDateTime zonedDateTime_now,Formula formula,Formate formate,Long digital) {
		if(zonedDateTime_now!=null){
			ZonedDateTime zonedDateTime_result =null;
			switch (formula.getValue()) {
			case "Plus":
				zonedDateTime_result = zonedDateTime_now.plusHours(digital);		
				break;
			case "Minus":
				zonedDateTime_result = zonedDateTime_now.minusHours(digital);				
				break;
			default:
				break;
			}
			final  DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			return zonedDateTime_result.format(formatter);
		}
		return null;
	}

	private String caculateDays(ZonedDateTime zonedDateTime_now,Formula formula,Formate formate,Long digital) {
		if(zonedDateTime_now!=null){
			ZonedDateTime zonedDateTime_result =null;
			switch (formula.getValue()) {
			case "Plus":
				zonedDateTime_result = zonedDateTime_now.plusDays(digital);		
				break;
			case "Minus":
				zonedDateTime_result = zonedDateTime_now.minusDays(digital);				
				break;
			default:
				break;
			}
			final  DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			return zonedDateTime_result.format(formatter);
		}
		return null;
	}
	
	private  String caculateMonths(ZonedDateTime zonedDateTime_now,Formula formula,Formate formate,Long digital) {
		if(zonedDateTime_now!=null){
			ZonedDateTime zonedDateTime_result =null;
			switch (formula.getValue()) {
			case "Plus":
				zonedDateTime_result = zonedDateTime_now.plusMonths(digital);		
				break;
			case "Minus":
				zonedDateTime_result = zonedDateTime_now.minusMonths(digital);				
				break;
			default:
				break;
			}
			final  DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			return zonedDateTime_result.format(formatter);
		}
		return null;
	}
	
	private  String caculateYears(ZonedDateTime zonedDateTime_now,Formula formula,Formate formate,Long digital) {
		if(zonedDateTime_now!=null){
			ZonedDateTime zonedDateTime_result =null;
			switch (formula.getValue()) {
			case "Plus":
				zonedDateTime_result = zonedDateTime_now.plusYears(digital);		
				break;
			case "Minus":
				zonedDateTime_result = zonedDateTime_now.minusYears(digital);				
				break;
			default:
				break;
			}
			final  DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			return zonedDateTime_result.format(formatter);
		}
		return null;
	}
	
	/**
	 * 
	 * @author daniel
	 * Get the duration by time
	 * @param startTimeString
	 * @param endTimeString
	 * @param formate
	 * @param duration_
	 * @return
	 */
	public Integer getDuration(String startTimeString,  String  endTimeString , Formate formate , Duration_ duration_){
		if(attributeCheck.stringsNotNull(startTimeString,endTimeString)){
			final DateTimeFormatter formatter = DateTimeFormatter.ofPattern(formate.getValue());
			LocalDateTime localDateStartTime = LocalDateTime.parse(startTimeString, formatter);	
			LocalDateTime localDateEndTime = LocalDateTime.parse(endTimeString, formatter);		
			switch (duration_.getValue()) {
			case "Nanos":
				return (int) java.time.Duration.between(localDateStartTime, localDateEndTime).toNanos();
			case "Millis":
				return (int) java.time.Duration.between(localDateStartTime, localDateEndTime).toMillis();
			case "Minutes":
				return (int) java.time.Duration.between(localDateStartTime, localDateEndTime).toMinutes();
			case "Hours":
				return (int) java.time.Duration.between(localDateStartTime, localDateEndTime).toHours();
			case "Days":
				return (int) java.time.Duration.between(localDateStartTime, localDateEndTime).toDays();	
			default:
				return null;
			}
		}else{
			return null;
		}
	}


	
}