import java.io.*;
import javax.lang.model.element.Element;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.w3c.dom.*;
public class DOM {
    static String arch;
    public static void main(String [] args) {

       if( args.length != 1) {
          System.out.println("error, debe de proporcionar el nombre del archivo");
          return;
       }
       arch=args[0];
       System.out.println("*****PROCESANDO EL DOM Del archivo "+arch);
       try {
          DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
          dbFactory.setValidating(true);
          DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
          dBuilder.setErrorHandler(MiErrorHandler.getErrorHandler());
          Document doc = dBuilder.parse(arch);
          System.out.println("********fin del analisis todo bien************");
          ProcesaDOM (doc);
       } catch (Exception e) {
          System.out.println("____________________________________________");
          System.out.println(e);
       }     
    }
    public static void ProcesaDOM(Node nodo) {
       switch (nodo.getNodeType()) {
       case Node.DOCUMENT_NODE:
          System.out.println("<%xml version=\"1.0\">");
          Document doc = (Document) nodo;
          ProcesaDOM(doc.getDocumentElement());
          break;
       case Node.ELEMENT_NODE:
          String nombre=nodo.getNodeName();
          System.out.println("<"+nombre+">");
          if(nodo.getChildNodes() != null) {
             for(int i=0 ; i<nodo.getChildNodes().getLength() ; i++) {
                for(int j=0 ; j< nodo.getAttributes().getLength() ; j++) {
                   ProcesaDOM(nodo.getAttributes().item(j));
                }
                ProcesaDOM(nodo.getChildNodes().item(i));
             }
          }
          System.out.println("</"+nombre+">");
          break;
       case Node.ATTRIBUTE_NODE:
          System.out.println(""+nodo.getNodeName()+"=\""+nodo.getNodeValue()+"\"");

          break;
       case Node.TEXT_NODE://"\n? *\n?"
          if (!nodo.getTextContent().matches("\n? *\n?"))
             System.out.println(nodo.getTextContent());
       }
    
    }
}
