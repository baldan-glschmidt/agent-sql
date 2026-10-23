# R349TII

## Descrição

S-5002 - eSocial - Totais de rendimentos tributáveis, deduções e isenções

---

## Resumo

- Campos: 28
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqTii | Number(009,0) | Não | Sequência Totais de rendimentos tributáveis, deduções e isenções |
| CRIrRt | Number(006,0) | Sim | Código de Receita para IR Retido na Fonte sobre rendimentos do trabalho |
| VlIrRt | Number(014,2) | Sim | Valor relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho |
| VlReTr | Number(014,2) | Sim | Valor relativo ao rendimento tributável mensal e férias |
| VlRt13 | Number(014,2) | Sim | Valor relativo ao rendimento do 13º salário |
| VlPrOf | Number(014,2) | Sim | Valor da previdência oficial sobre rendimentos do trabalho, mensal e férias |
| VlPo13 | Number(014,2) | Sim | Valor relativo à previdência oficial sobre o 13° salário |
| VlCr13 | Number(014,2) | Sim | IR retido na fonte sobre rendimentos do trabalho e 13° salário |
| VlPi65 | Number(014,2) | Sim | Isenção de aposentadoria, reserva, reforma e pensão para maiores de 65 anos |
| VPi65d | Number(014,2) | Sim | Isenção de aposentadoria, reserva, reforma e pensão para maiores de 65 anos 13° |
| VlrDia | Number(014,2) | Sim | Valor relativo a diárias |
| VlAjCu | Number(014,2) | Sim | Valor relativo à ajuda de custo |
| VlInRe | Number(014,2) | Sim | Valor da indenização e rescisão de contrato, incluindo PDV e acidentes |
| VlAbPe | Number(014,2) | Sim | Valor relativo ao abono pecuniário |
| VlMoGr | Number(014,2) | Sim | Valor referente a rendimento de beneficiário com moléstia grave ou acidente |
| VlMoGd | Number(014,2) | Sim | Valor do 13º salário para beneficiário com moléstia grave ou acidente em serviço |
| VlAuMo | Number(014,2) | Sim | Valor relativo ao auxílio-moradia |
| VlBoMe | Number(014,2) | Sim | Valor relativo à bolsa médico residente |
| VlBm13 | Number(014,2) | Sim | Valor relativo à bolsa médico residente - 13º salário |
| VlJuMo | Number(014,2) | Sim | Valor dos juros de mora por atraso na remuneração de emprego, cargo ou função |
| VlIsOu | Number(014,2) | Sim | Valor relativo aos rendimentos isentos - outros |
| DesRen | String(999) | Sim | Descrição do rendimento não tributável ou isento do IRRF |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqTii

---

## Índices

### R349TIIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
