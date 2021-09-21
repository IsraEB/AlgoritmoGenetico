/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UI;

import javax.swing.border.Border;
import java.awt.Component;
import java.awt.Graphics;
import java.awt.Insets;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

import javax.swing.JOptionPane;

/**
 *
 * @author lolyc
 */
public class MainFrame extends javax.swing.JFrame {
    /**
     * Creates new form MainFrame
     */
    public MainFrame() {
        initComponents();
        btnMinimizar.setBorder(new RoundedBorder(5));
        btnMaximizar.setBorder(new RoundedBorder(5));
    }

    // <editor-fold defaultstate="collapsed" desc="Generated
    // <editor-fold defaultstate="collapsed" desc="Generated
    // <editor-fold defaultstate="collapsed" desc="Generated
    // <editor-fold defaultstate="collapsed" desc="Generated
    // Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        buttonGroup1 = new javax.swing.ButtonGroup();
        jPanel1 = new javax.swing.JPanel();
        jLabel2 = new javax.swing.JLabel();
        txtPIni = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();
        txtNGen = new javax.swing.JTextField();
        rbMejores = new javax.swing.JRadioButton();
        rbTorneo = new javax.swing.JRadioButton();
        btnMinimizar = new javax.swing.JButton();
        btnMaximizar = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Evolucion diferencial");

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "F(x) = x2 + y3 + z4    (x, y, z) ",
                javax.swing.border.TitledBorder.CENTER, javax.swing.border.TitledBorder.DEFAULT_POSITION,
                new java.awt.Font("Consolas", 1, 14))); // NOI18N

        jLabel2.setFont(new java.awt.Font("Consolas", 1, 12)); // NOI18N
        jLabel2.setText("Numero de individuos de población inicial [MIN=4]:");

        txtPIni.setText("4");
        txtPIni.setCursor(new java.awt.Cursor(java.awt.Cursor.TEXT_CURSOR));

        jLabel3.setFont(new java.awt.Font("Consolas", 1, 12)); // NOI18N
        jLabel3.setText("Numero de generaciones[MAX=4]:");

        txtNGen.setText("4");

        buttonGroup1.add(rbMejores);
        rbMejores.setText("Selección por mejores pobladores");

        buttonGroup1.add(rbTorneo);
        rbTorneo.setSelected(true);
        rbTorneo.setText("Selección por torneo con un punto de cruza");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(jPanel1Layout.createSequentialGroup().addContainerGap().addGroup(jPanel1Layout
                        .createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(jPanel1Layout.createSequentialGroup().addComponent(rbTorneo)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED,
                                        javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(rbMejores))
                        .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 220,
                                        javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 197,
                                        Short.MAX_VALUE)
                                .addComponent(txtNGen, javax.swing.GroupLayout.PREFERRED_SIZE, 88,
                                        javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(javax.swing.GroupLayout.Alignment.TRAILING,
                                jPanel1Layout.createSequentialGroup().addGap(0, 0, Short.MAX_VALUE).addComponent(
                                        txtPIni, javax.swing.GroupLayout.PREFERRED_SIZE, 88,
                                        javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addGap(37, 37, 37))
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(jPanel1Layout.createSequentialGroup().addContainerGap().addComponent(jLabel2)
                                .addContainerGap(192, Short.MAX_VALUE))));
        jPanel1Layout.setVerticalGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(jPanel1Layout.createSequentialGroup().addContainerGap()
                        .addComponent(txtPIni, javax.swing.GroupLayout.PREFERRED_SIZE, 20,
                                javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(45, 45, 45)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                .addComponent(txtNGen, javax.swing.GroupLayout.PREFERRED_SIZE,
                                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(jLabel3))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 30, Short.MAX_VALUE)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                .addComponent(rbMejores).addComponent(rbTorneo))
                        .addGap(28, 28, 28))
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(jPanel1Layout.createSequentialGroup().addGap(17, 17, 17).addComponent(jLabel2)
                                .addContainerGap(145, Short.MAX_VALUE))));

        btnMinimizar.setText("Minimizar");
        btnMinimizar.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        btnMinimizar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnMinimizarActionPerformed(evt);
            }
        });

        btnMaximizar.setText("Maximizar");
        btnMaximizar.setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        btnMaximizar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnMaximizarActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup().addGap(71, 71, 71)
                        .addComponent(btnMinimizar, javax.swing.GroupLayout.PREFERRED_SIZE, 99,
                                javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 177, Short.MAX_VALUE)
                        .addComponent(btnMaximizar, javax.swing.GroupLayout.PREFERRED_SIZE, 99,
                                javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(82, 82, 82))
                .addGroup(layout.createSequentialGroup().addContainerGap().addComponent(jPanel1,
                        javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addContainerGap()));
        layout.setVerticalGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(layout.createSequentialGroup().addContainerGap()
                        .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE,
                                javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(31, 31, 31)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                .addComponent(btnMaximizar).addComponent(btnMinimizar))
                        .addContainerGap(27, Short.MAX_VALUE)));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnMinimizarActionPerformed(java.awt.event.ActionEvent evt) {// GEN-FIRST:event_btnMinimizarActionPerformed

        int nPoblación, nGeneraciones;

        try {
            nPoblación = Integer.parseInt(txtPIni.getText());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Número de individuos incorrecta", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        try {
            nGeneraciones = Integer.parseInt(txtNGen.getText());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Número de generaciones incorrecta", "Error",
                    JOptionPane.ERROR_MESSAGE);
            return;
        }

        if (nPoblación < 4) {
            JOptionPane.showMessageDialog(this, "Se necesitan al menos 4 individuos para hacer el algoritmo", "Error",
                    JOptionPane.ERROR_MESSAGE);
            return;
        }

        if (nGeneraciones > 4) {
            JOptionPane.showMessageDialog(this, "El máximo de generaciones son 4", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        String filename;
        if (rbMejores.isSelected()) {
            filename = "\".\\src\\logic\\Genetic algorithm.py\"";
        } else {
            filename = "\".\\src\\logic\\Genetic algorithm - Ledezma method.py\"";
        }

        String cmd = "cmd /c python " + filename + " " + nPoblación + " " + nGeneraciones + " Minimize";

        System.out.println(cmd);

        Runtime run = Runtime.getRuntime();
        try {
            Process pr = run.exec(cmd);
            pr.waitFor();
            BufferedReader buf = new BufferedReader(new InputStreamReader(pr.getInputStream()));
            String line = "";
            while ((line = buf.readLine()) != null) {
                System.out.println(line);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Ocurrió un error");
        }

        try {
            String content = Files.readString(Path.of(".\\src\\logic\\output.txt"), StandardCharsets.US_ASCII);
            Mostrar mostrar = new Mostrar();

            mostrar.setTipo("Minimizar");

            mostrar.addContenido(content);

            mostrar.setVisible(true);
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Ocurrió un error");
        }

    }// GEN-LAST:event_btnMinimizarActionPerformed

    private void btnMaximizarActionPerformed(java.awt.event.ActionEvent evt) {// GEN-FIRST:event_btnMaximizarActionPerformed
        int nPoblación, nGeneraciones;

        try {
            nPoblación = Integer.parseInt(txtPIni.getText());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Número de individuos incorrecta", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        try {
            nGeneraciones = Integer.parseInt(txtNGen.getText());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Número de generaciones incorrecta", "Error",
                    JOptionPane.ERROR_MESSAGE);
            return;
        }

        if (nPoblación < 4) {
            JOptionPane.showMessageDialog(this, "Se necesitan al menos 4 individuos para hacer el algoritmo", "Error",
                    JOptionPane.ERROR_MESSAGE);
            return;
        }

        if (nGeneraciones > 4) {
            JOptionPane.showMessageDialog(this, "El máximo de generaciones son 4", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        String filename;
        if (rbMejores.isSelected()) {
            filename = "\".\\src\\logic\\Genetic algorithm.py\"";
        } else {
            filename = "\".\\src\\logic\\Genetic algorithm - Ledezma method.py\"";
        }

        String cmd = "cmd /c python " + filename + " " + nPoblación + " " + nGeneraciones + " Maximize";

        System.out.println(cmd);

        Runtime run = Runtime.getRuntime();
        try {
            Process pr = run.exec(cmd);
            pr.waitFor();
            BufferedReader buf = new BufferedReader(new InputStreamReader(pr.getInputStream()));
            String line = "";
            while ((line = buf.readLine()) != null) {
                System.out.println(line);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Ocurrió un error");
        }

        try {
            String content = Files.readString(Path.of(".\\src\\logic\\output.txt"), StandardCharsets.US_ASCII);
            Mostrar mostrar = new Mostrar();

            mostrar.setTipo("Maximizar");

            mostrar.addContenido(content);

            mostrar.setVisible(true);
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Ocurrió un error");
        }

    }// GEN-LAST:event_btnMaximizarActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        // <editor-fold defaultstate="collapsed" desc=" Look and feel setting code
        // (optional) ">
        /*
         * If Nimbus (introduced in Java SE 6) is not available, stay with the default
         * look and feel. For details see
         * http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(MainFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        // </editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new MainFrame().setVisible(true);

            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnMaximizar;
    private javax.swing.JButton btnMinimizar;
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JRadioButton rbMejores;
    private javax.swing.JRadioButton rbTorneo;
    private javax.swing.JTextField txtNGen;
    private javax.swing.JTextField txtPIni;
    // End of variables declaration//GEN-END:variables

    private static class RoundedBorder implements Border {
        private int radius;

        RoundedBorder(int radius) {
            this.radius = radius;
        }

        public Insets getBorderInsets(Component c) {
            return new Insets(this.radius + 1, this.radius + 1, this.radius + 2, this.radius);
        }

        public boolean isBorderOpaque() {
            return true;
        }

        public void paintBorder(Component c, Graphics g, int x, int y, int width, int height) {
            g.drawRoundRect(x, y, width - 1, height - 1, radius, radius);
        }
    }
}
