# R349PRV

## Descrição

S-5002 - eSocial - Informações de planos de previdência complementar

---

## Resumo

- Campos: 16
- Chave Primária: 8 campo(s)
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
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqCri | Number(009,0) | Não | Sequência |
| SeqPrv | Number(009,0) | Não | Sequência |
| TipPrv | Number(001,0) | Sim | Tipo de previdência complementar |
| NumPrv | Number(014,0) | Sim | CNPJ da Entidade de Previdência Complementar |
| CfjPrv | String(014) | Sim | CNPJ da Entidade de Previdência Complementar |
| VlrDed | Number(014,2) | Sim | Valor da dedução relativa a previdência complementar |
| VlrPtr | Number(014,2) | Sim | Valor da contribuição do ente público patrocinador da Fundação de Previdência Complementar do Servidor Público (Funpresp) |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| VlDe13 | Number(014,2) | Sim | Valor da dedução do 13º Salário relativo à previdência complementar |
| VlFu13 | Number(014,2) | Sim | Valor da contribuição do 13º salário do ente público para a Funpresp |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqCri
- SeqPrv

---

## Índices

### R349PRVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
