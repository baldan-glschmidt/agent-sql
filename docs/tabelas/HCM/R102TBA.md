# R102TBA

## Descrição

Trabalhos do SESMT - Áreas Não Relac. Organograma

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTbr | Number(006,0) | Não | Código do Trabalho |
| SeqTbr | Number(003,0) | Não | Sequência que individualiza a área |
| LocTbr | String(050) | Sim | Descrição do local de realização do trabalho |

---

## Chave Primária

- NumEmp
- CodTbr
- SeqTbr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102TBA_001

**Tabela:** R102TBR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodTbr | CodTbr |

