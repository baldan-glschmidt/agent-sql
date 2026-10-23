# R352BSF

## Descrição

S-5503 - Informações sobre bases de cálculo e valores do FGTS por período de referência

---

## Resumo

- Campos: 17
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| SeqFgt | Number(002,0) | Não | Sequência informações FGTS |
| SeqIft | Number(002,0) | Não | Sequência Matrícula |
| SeqBsf | Number(002,0) | Não | Sequência Informações base de cálculo |
| PerRef | Date | Não | Mês/ano de referência das informações |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| TipVlr | Number(002,0) | Sim | Tipo de valor que influi na apuração do FGTS |
| BcFgNd | Number(015,2) | Sim | Valor da base de cálculo de FGTS ainda não declarada, reconhecida no processo trabalhista |
| BcFgHi | Number(015,2) | Sim | Valor histórico do FGTS a ser depositado na conta vinculada do trabalhador sobre base reconhecida no processo trabalhista |
| BcFgDe | Number(015,2) | Sim | Valor da base de cálculo declarada anteriormente em SEFIP e ainda não recolhida |
| VlrFDe | Number(015,2) | Sim | Valor histórico do FGTS a ser depositado na conta vinculada do trabalhador sobre base já declarada anteriormente em SEFIP |
| BcFgNr | Number(015,2) | Sim | Valor da base de cálculo declarada anteriormente no eSocial e ainda não recolhida |
| BcFgRe | Number(015,2) | Sim | Valor histórico do FGTS a ser depositado na conta vinculada do trabalhador sobre base já declarada anteriormente no eSocial |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- SeqFgt
- SeqIft
- SeqBsf

---

## Índices

### R352BSFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
