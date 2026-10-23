# R059LBI

## Descrição

Cadastro de leitoras biométricas

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodLei | Number(003,0) | Não | Código da Leitora |
| DesLei | String(030) | Sim | Descrição da Leitora |
| CodTBi | Number(002,0) | Sim | Código da Tecnologia Biométrica |
| LocLei | String(020) | Sim | Localização da Leitora (Máquina da Rede) |
| PorLei | Number(005,0) | Sim | Porta  da leitora |

---

## Chave Primária

- CodLei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R059LBI_002

**Tabela:** R058BIO

| Origem | Destino |
|--------|---------|
| CodTBi | CodTBi |

