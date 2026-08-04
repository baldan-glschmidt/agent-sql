# E140AVA

## Descrição

Vendas - Notas Fiscais de Saída - Avalistas

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqAva | Number(008,0) | Não | Sequência dos avalistas |
| CodAva | Number(009,0) | Não | Código do Avalista |
| VlrFin | Number(015,2) | Sim | Valor líquido da nota fiscal para o financeiro |
| ObsNfv | String(250) | Sim | Texto da observação da nota fiscal de saída |
| ObsAva | String(250) | Sim | Texto do avalista |
| SitAva | String(001) | Sim | Situação da observação |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqAva

---

## Índices

### E140AVAIndice1

**Tipo:** Não unico

Campos:
- CodAva

---

## Relacionamentos

### IR_E140AVA_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140AVA_005

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodAva | CodCli |

