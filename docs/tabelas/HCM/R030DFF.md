# R030DFF

## Descrição

Empresas - Desoneração da Folha - Filial Empregadora

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração da Busca de Receitas |
| BusRec | Number(001,0) | Sim | Buscar Receita Desoneração |
| Rec13s | Number(001,0) | Sim | Receita para Desoneração 13° Salário |
| DesDis | Number(001,0) | Sim | Forma de Cálculo para Desoneração Dissídio |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030DFF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R030DFF_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

