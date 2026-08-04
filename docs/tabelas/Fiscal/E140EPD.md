# E140EPD

## Descrição

Vendas - Notas Fiscais de Saída - Conteúdo das Embalagens

---

## Resumo

- Campos: 15
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqEmb | Number(006,0) | Não | Sequência de embalagem |
| SeqEpd | Number(004,0) | Não | Sequência do Conteúdo das Embalagens |
| SeqIpv | Number(003,0) | Não | Sequência do item de produto da nota fiscal de saída |
| SeqEbi | Number(006,0) | Sim | Sequência da Embalagem Intermediária |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
| NumEmb | String(030) | Sim | Número da embalagem de Estocagem |
| QtdPro | Number(014,5) | Sim | Quantidade do produto na embalagem |
| PesBru | Number(014,5) | Sim | Peso bruto do produto |
| PesLiq | Number(014,5) | Sim | Peso líquido do produto |
| ObsPro | String(250) | Sim | Texto da observação do produto na embalagem |
| CodBa2 | String(030) | Sim | Código de barras livre |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqEmb
- SeqEpd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140EPD_004

**Tabela:** E140EMB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqEmb | SeqEmb |

