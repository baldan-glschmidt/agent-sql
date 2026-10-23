# R020TOM

## Descrição

Rateios - Tomadores

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRat | Number(009,0) | Não | Código do Rateio |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTom | Number(008,0) | Sim | Código do Tomador de Serviço |
| CodFil | Number(006,0) | Sim | Código da Filial |

---

## Chave Primária

- CodRat
- NumEmp

---

## Índices

### R020TOMIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- CodFil

---

## Relacionamentos

### IR_R020TOM_000

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

