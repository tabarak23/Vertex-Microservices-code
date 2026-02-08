package com.example.order.service;

import com.example.order.dto.OrderRequest;
import com.example.order.model.OrderEntity;
import com.example.order.repository.OrderRepository;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.boot.web.client.RestTemplateBuilder;

import java.time.Duration;
import java.util.List;

@Service
public class OrderService {

    private final OrderRepository repo;
    private final RestTemplate rest;

    @Value("${USER_SERVICE_URL}")
    private String userService;

    @Value("${PRODUCT_SERVICE_URL}")
    private String productService;

    public OrderService(OrderRepository repo, RestTemplateBuilder builder) {
        this.repo = repo;
        this.rest = builder
                .setConnectTimeout(Duration.ofSeconds(2))
                .build();
    }

    public OrderEntity createOrder(OrderRequest req) {
        rest.getForEntity(
                userService + "/api/v1/users/" + req.getUserId(),
                String.class
        );

        rest.getForEntity(
                productService + "/api/v1/products/" + req.getProductId(),
                String.class
        );

        OrderEntity order = new OrderEntity(
                req.getUserId(),
                req.getProductId(),
                req.getQuantity()
        );

        return repo.save(order);
    }

    public OrderEntity getOrder(Long id) {
        return repo.findById(id).orElseThrow();
    }

    public List<OrderEntity> listByUser(Long userId) {
        return repo.findByUserId(userId);
    }
}

