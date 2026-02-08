package com.example.order.controller;

import com.example.order.dto.OrderRequest;
import com.example.order.model.OrderEntity;
import com.example.order.service.OrderService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/orders")
public class OrderController {

    private final OrderService service;

    public OrderController(OrderService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<OrderEntity> create(@RequestBody OrderRequest req) {
        return ResponseEntity.ok(service.createOrder(req));
    }

    @GetMapping("/{id}")
    public ResponseEntity<OrderEntity> get(@PathVariable Long id) {
        return ResponseEntity.ok(service.getOrder(id));
    }

    @GetMapping("/user/{userId}")
    public ResponseEntity<List<OrderEntity>> listByUser(@PathVariable Long userId) {
        return ResponseEntity.ok(service.listByUser(userId));
    }
}

