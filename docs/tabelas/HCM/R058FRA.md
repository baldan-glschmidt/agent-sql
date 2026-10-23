# R058FRA

## Descrição

Funções Restritas do Acesso

---

## Resumo

- Campos: 3
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFra | Number(002,0) | Não | Código da Função Restrita do Acesso |
| DesFra | String(030) | Sim | Descrição da Função Restrita |
| CodFnc | Number(002,0) | Sim | Codigo da Função do Coletor |

---

## Chave Primária

- CodFra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058FRA_002

**Tabela:** R058FNC

| Origem | Destino |
|--------|---------|
| CodFnc | CodFnc |

