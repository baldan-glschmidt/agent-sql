# E210MMF

## Descrição

Estoques - Preço Médio Mensal Fixo

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| MesAno | Date | Não | Mês e ano correspondente as informações |
| QtdMmf | Number(014,5) | Sim | Saldo em quantidade no mês para média mensal fixa |
| VlrMmf | Number(015,2) | Sim | Saldo em valor no mês para média mensal fixa |
| IcmMmf | Number(015,2) | Sim | Saldo em valor de ICMS no mês para média mensal fixa |
| PrmMmf | Number(015,6) | Sim | Preço médio mensal fixo |
| PmiMmf | Number(015,6) | Sim | Preço médio mensal fixo de ICMS |
| DatGer | Date | Sim | Data base da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geraçao do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SalMes | String(001) | Sim | Este saldo corresponde ao mês atual ou foi buscado de outro mês? |
| PreFix | Number(015,6) | Sim | Custo médio fixo |
| IcmFix | Number(019,6) | Sim | Valor do ICMS médio fixo dos produtos acabados |
| USU_PreFix | Number(015,6) | Sim | Custo médio fixo |
| USU_ICMFIX | Number(015,6) | Sim | Valor do ICMS médio fixo |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro
- CodDer
- MesAno

---

## Índices

### E210MMFIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

---

## Relacionamentos

### IR_E210MMF_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E210MMF_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E210MMF_002

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E210MMF_003

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

