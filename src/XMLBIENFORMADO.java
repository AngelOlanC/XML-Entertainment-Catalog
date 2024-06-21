import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;

public class XMLBIENFORMADO {
    public static void main(String [] args) {
       if( args.length != 1) {
          System.out.println("error, debe de proporcionar el nombre del archivo");
          return;
       }
       String arch=args[0];
       System.out.println("*****VALIDADNDO SI ESTÁ BIEN FORMADOS EL ARCHIVO "+arch);
       try {
          DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();

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
