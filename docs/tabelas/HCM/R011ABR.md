# R011ABR

## Descrição

Abrangências do Banco de Horas

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBHr | Number(005,0) | Não | Código do Banco de Horas |
| CamRef | String(006) | Não | Campo de Referência para Abrangência |
| AbrCam | String(1000) | Sim | Abrangência do Campo |

---

## Chave Primária

- CodBHr
- CamRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011ABR_000

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBHr | CodBHr |

