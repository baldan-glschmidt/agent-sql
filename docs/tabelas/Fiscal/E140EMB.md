# E140EMB

## Descrição

Vendas - Notas Fiscais de Saída - Embalagens

---

## Resumo

- Campos: 15
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
| SeqEmb | Number(006,0) | Não | Sequência de embalagem |
| CodEmb | Number(004,0) | Não | Código da embalagem |
| QtdEmb | Number(006,0) | Sim | Quantidade de embalagens |
| NumEmb | String(030) | Sim | Números das embalagens |
| NumNiv | Number(002,0) | Sim | Nível da Embalagem |
| PesBru | Number(014,5) | Sim | Peso bruto das embalagens e produtos |
| PesLiq | Number(014,5) | Sim | Peso líquido dos produtos |
| ObsEmb | String(250) | Sim | Texto da observação das embalagens |
| NumSdx | Number(008,0) | Sim | Número do Sedex no qual as mercadorias foram enviadas |
| StrSdx | String(020) | Sim | Número do Sedex completo no formato do correio |
| CodBa2 | String(030) | Sim | Código de barras livre |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqEmb

---

## Índices

### E140EMBIndice1

**Tipo:** Não unico

Campos:
- CodEmb

---

## Relacionamentos

### IR_E140EMB_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140EMB_005

**Tabela:** E059EMB

| Origem | Destino |
|--------|---------|
| CodEmb | CodEmb |

