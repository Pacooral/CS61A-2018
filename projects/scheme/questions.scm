(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.



(define (cons-all num rests) 
    (map (lambda (x) (cons num x)) rests)
)

(define (enumerate s)
  (define (iter1 n s)
      (if (null? s) 
          nil 
          (cons (list n (car s))
                (iter1 (+ n 1) (cdr s) ))
      )
      )
    (iter1 0 s)
)




;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (define (change rest num)
    (cond ((= rest 0)) 
      )
    )
  )
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (zip pairs) (cons (map car pairs) (map cdar pairs)) )
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (cons form (cons params (let-to-lambda body)))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (cons ())
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (cons (car expr) (map let-to-lambda (cdr expr)))
         ; END PROBLEM 18
         )))