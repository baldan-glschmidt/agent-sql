# R030DFO

## Descrição

Empresas - Desoneração da Folha

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatAlt | Date | Não | Data Alteração da Busca de Receitas |
| BusRec | Number(001,0) | Sim | Buscar Receita Desoneração |
| Rec13s | Number(001,0) | Sim | Receita para Desoneração 13° Salário |
| DesDis | Number(001,0) | Sim | Forma de Cálculo para Desoneração Dissídio |

---

## Chave Primária

- NumEmp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030DFO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

