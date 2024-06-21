import org.w3c.dom.Document;
import org.w3c.dom.NameList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;


public class XMLVALIDO {
    public static void main(String [] args) {
       if( args.length != 1) {
          System.out.println("error, debe de proporcionar el nombre del archivo");
          return;
       }
       String arch=args[0];
       System.out.println("*****VALIDADNDO, SI ES VALIDO EL ARCHIVO "+arch);
       try {
          DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
          dbFactory.setValidating(true);
          DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
          dBuilder.setErrorHandler(MiErrorHandler.getErrorHandler());
          Document doc = dBuilder.parse(arch);

          System.out.println("********fin del analisis todo bien************");
    } 
       catch (Exception e) {
          System.out.println("_______________________________________");
          System.out.println(e);
          return;
       }     
    }
}
