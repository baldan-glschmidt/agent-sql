# E055EST

## Descrição

Cadastros - Tributos - Parâmetros de Configuração do Estoque

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| CodTst | String(003) | Sim | Situação tributária do ICMS |
| MudTri | String(001) | Sim | Mudança na forma de tributação do ICMS (art. 4 Portaria CAT 26/2015) |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- CodPro
- CodDer

---

## Índices

### E055ESTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro

---

## Relacionamentos

### IR_E055EST_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E055EST_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

### IR_E055EST_004

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

