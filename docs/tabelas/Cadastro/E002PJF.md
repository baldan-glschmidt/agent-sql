# E002PJF

## Descrição

Cadastros - Finanças - Parâmetros Ajustes Financeiros

---

## Resumo

- Campos: 24
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador dos parâmetros do ajuste |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SitReg | String(001) | Não | Situação do registro |
| AplAjf | String(001) | Sim | Aplicação dos parâmetros de ajustes financeiros a receber ou pagar |
| AvpTpa | String(001) | Não | Tipo da periodicidade para cálculo do prazo do ajuste a valor presente |
| AvpPmi | Number(003,0) | Não | Período mínimo para o cálculo do ajuste a valor presente |
| AvpDra | Number(001,0) | Não | Dia para o registro do ajuste a valor presente |
| AvpVta | Number(015,2) | Sim | Valor mínimo do título para o cálculo do ajuste a valor presente |
| AvpTra | String(005) | Não | Transação padrão para o rateio do ajuste a valor presente |
| AvpTpc | Number(001,0) | Não | Tipo do cálculo para a taxa ajuste a valor presente |
| AvpQtp | Number(009,0) | Não | Quantidade de títulos por pacote de processamento do ajuste a valor presente |
| AvpMpa | String(003) | Não | Código da moeda para o cálculo do ajuste a valor presente |
| AvpTdb | Number(001,0) | Não | Tipo da data base para o cálculo do ajuste a valor presente |
| AvpTvr | Number(001,0) | Não | Tipo do valor de referência para cálculo do ajuste a valor presente |
| AvpCtn | String(001) | Não | Considera títulos com origem em nota fiscal |
| ConFpe | String(001) | Sim | Considerar Fração de Período para Cálculo |
| TpeAvp | String(001) | Sim | Momento de Execução AVP |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E002PJFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- AplAjf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
