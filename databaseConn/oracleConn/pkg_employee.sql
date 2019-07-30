/*
 Author - Prashant Acharya
 Date   - 19/May/2019
*/

CREATE OR REPLACE PACKAGE employee_dtls 
AS 
    FUNCTION get_dtls( pv_job_id IN jobs.job_id%TYPE DEFAULT NULL )
        RETURN SYS_REFCURSOR;
        
    FUNCTION get_emp_dtls( pv_job_id IN jobs.job_id%TYPE DEFAULT NULL )
        RETURN SYS_REFCURSOR;
    
END employee_dtls;
/

SHO ERRORS


/*
 Author - Prashant Acharya
 Date   - 19/May/2019
*/
CREATE OR REPLACE PACKAGE BODY employee_dtls
AS

    FUNCTION job_id_exists ( pv_job_id IN jobs.job_id%TYPE )
        RETURN BOOLEAN
    AS
        lv_exists NUMBER;
    BEGIN
        BEGIN
        
            SELECT 1
            INTO lv_exists
            FROM jobs
            WHERE job_id = pv_job_id;
            
            RETURN TRUE;
            
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                RETURN FALSE;
            WHEN TOO_MANY_ROWS THEN
                RETURN FALSE;
        END;
    END job_id_exists;

    FUNCTION get_dtls( pv_job_id IN jobs.job_id%TYPE DEFAULT NULL )
        RETURN SYS_REFCURSOR
    AS
        lv_results SYS_REFCURSOR;
    BEGIN
        IF ( pv_job_id IS NOT NULL )
        THEN
            IF ( job_id_exists ( pv_job_id => pv_job_id ) )
            THEN            
                OPEN lv_results FOR
                    SELECT JSON_OBJECT (
                               'department' value d.department_name,
                               'employees' value JSON_ARRAYAGG (
                                  JSON_OBJECT (
                                    'name' value first_name || ',' || last_name, 
                                    'job' value job_title )))
                    FROM departments d, 
                         employees e, 
                         jobs j
                    WHERE d.department_id = e.department_id 
                      AND e.job_id = j.job_id 
                      AND j.job_id = pv_job_id
                    GROUP BY d.department_name;
            ELSE
                RAISE_APPLICATION_ERROR( -20010, 'The job-id provided does not exist in the database. Please check and resubmit request');
            END IF;
        ELSE
            OPEN lv_results FOR
                SELECT JSON_OBJECT (
                           'department' value d.department_name,
                           'employees' value JSON_ARRAYAGG (
                              JSON_OBJECT (
                                'name' value first_name || ',' || last_name, 
                                'job' value job_title )))
                FROM departments d, 
                     employees e, 
                     jobs j
                WHERE d.department_id = e.department_id 
                  AND e.job_id = j.job_id 
                GROUP BY d.department_name;            
        END IF;

        RETURN lv_results;
    EXCEPTION
        WHEN OTHERS THEN
            RAISE;
    END get_dtls;
                                  
    FUNCTION get_emp_dtls( pv_job_id IN jobs.job_id%TYPE DEFAULT NULL )
        RETURN SYS_REFCURSOR
    AS
        lv_results SYS_REFCURSOR;
    BEGIN
        IF ( pv_job_id IS NOT NULL )
        THEN
            IF ( job_id_exists ( pv_job_id => pv_job_id ) )
            THEN
                OPEN lv_results FOR
                    SELECT department_name AS department_name,
                           first_name||','||last_name AS name,
                           job_title AS job
                    FROM departments d, 
                         employees e, 
                         jobs j
                    WHERE d.department_id = e.department_id 
                      AND e.job_id = j.job_id
                      AND j.job_id = pv_job_id
                    ORDER BY d.department_name;  
            ELSE
                RAISE_APPLICATION_ERROR( -20010, 'The job-id provided does not exist in the database. Please check and resubmit request');
            END IF;
        ELSE
            OPEN lv_results FOR
                SELECT department_name, listagg(job_title||'~'||first_name||','||last_name, '%')
                WITHIN GROUP (ORDER BY department_name)
                FROM departments d,
                     employees e,
                     jobs j
                WHERE d.department_id = e.department_id
                  AND e.job_id = j.job_id
                GROUP BY d.department_name;
        END IF;
        
        RETURN lv_results;
    END get_emp_dtls;
END employee_dtls;
/

SHO ERRORS   
