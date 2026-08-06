# Write your MySQL query statement below
SELECT ROUND(AVG(d.order_date=d.customer_pref_delivery_date)*100,2) AS immediate_percentage
FROM Delivery d
JOIN (
    SELECT customer_id,
    
    MIN(order_date) as first_order
    FROM Delivery f
    group by customer_id

) as f
ON d.customer_id=f.customer_id AND d.order_date=f.first_order