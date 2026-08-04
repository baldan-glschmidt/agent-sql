# E700CTM

## Descrição

Ficha - Modelo - Consumo Componente por Derivação

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
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção onde o Componente é agregado ao Produto composto |
| SeqMod | Number(004,0) | Não | Sequência lógica onde o Componente é utilizado na fabricação do Produto composto |
| CodDer | String(007) | Não | Derivação associada ao Modelo |
| CodCmp | String(014) | Não | Código do Componente (Produto) |
| DerCmp | String(007) | Sim | Derivação do Componente FIXA (p/ todos os Produtos compostos que estão associados) |
| QtdUti | Number(014,5) | Não | Quantidade utilizada do componente (Proporcional/Fixa) |
| QtdFrq | Number(014,5) | Sim | Quantidade Frequencial (Produto produzido) que o componente é consumido (apropriado) |
| PerPrd | Number(006,3) | Sim | % Perda do componente no processo de fabricação |
| PrdQtd | Number(014,5) | Não | Quantidade de perda do componente no processo de fabricação |
| UniMe2 | String(003) | Não | Unidade de medida  do componente na Produção |
| DatAlt | Date | Sim | Data da Alteração |
| CodUsu | Number(010,0) | Sim | Código do Usuário que alterou o registro |
| CodVac | String(005) | Sim | Código da variação p/ utilização no consumo do Modelo |
| BxaOrp | String(001) | Sim | Se for componente de alguma OP, indica se o mesmo é baixado |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodMod
- CodEtg
- SeqMod
- CodDer

---

## Índices

### E700CTMIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodCmp
- DerCmp

---

## Relacionamentos

### IR_E700CTM_003

**Tabela:** E700CMM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |
| CodEtg | CodEtg |
| SeqMod | SeqMod |

### IR_E700CTM_004

**Tabela:** E700DMO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |
| CodDer | CodDer |

### IR_E700CTM_005

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCmp | CodPro |

### IR_E700CTM_011

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMe2 | UniMed |

