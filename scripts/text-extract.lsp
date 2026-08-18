;; text-extract.lsp
;; Extract text and MText entities to a CSV file
;; Run command: TEXTEXPORT
;; Tested with GSTARCAD 2024-2026
(defun c:TEXTEXPORT (/ ss i ent txt fh)
  (if (setq ss (ssget '((0 . "TEXT,MTEXT"))))
    (progn
      (setq fh (open (getfiled "Save text export" "" "csv" 1) "w"))
      (if fh
        (progn
          (setq i 0)
          (repeat (sslength ss)
            (setq ent (entget (ssname ss i)))
            (setq txt (cdr (assoc 1 ent)))
            (if txt
              (write-line (strcat "\"" txt "\"") fh)
            )
            (setq i (1+ i))
          )
          (close fh)
          (princ (strcat "\nExported " (itoa (sslength ss)) " text entities."))
        )
      )
    )
  )
  (princ)
)