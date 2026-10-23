# R350EPI

## Descrição

S-2240 - eSocial - Condições Ambientais do Trabalho - EPIs

---

## Resumo

- Campos: 18
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data em que o trabalhador iniciou as atividades no ambiente de trabalho |
| SeqCon | Number(009,0) | Não | Sequência |
| SeqFrc | Number(009,0) | Não | Sequência Fator Risco |
| SeqEpi | Number(009,0) | Não | Sequência EPI |
| CerApr | String(255) | Sim | Certificado de Aprovação do Equipamento de Proteção Individual |
| DesEpi | String(999) | Sim | Descrição do Equipamento de Proteção Individual |
| EfiEpi | String(001) | Sim | O EPI é eficaz na neutralização do risco ao trabalhador? |
| MedPro | String(001) | Sim | Foi tentada a implementação de medidas de proteção coletiva? (Obsoleto) |
| ConFun | String(001) | Sim | Foram observadas as condições de funcionamento do EPI ao longo do tempo? (Obsoleto) |
| UsoIni | String(001) | Sim | Foi observado o uso ininterrupto do EPI ao longo do tempo? (Obsoleto) |
| PraVal | String(001) | Sim | Foi observado o prazo de validade do Certificado de Aprovação - CA do MTb? (Obsoleto) |
| PerTro | String(001) | Sim | É observada a periodicidade de troca definida pelo fabricante nacional ou importador e/ou programas ambientais? (Obsoleto) |
| ObsHig | String(001) | Sim | É observada a higienização conforme orientação do fabricante nacional ou importador? (Obsoleto) |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatIni
- SeqCon
- SeqFrc
- SeqEpi

---

## Índices

### R350EPIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
