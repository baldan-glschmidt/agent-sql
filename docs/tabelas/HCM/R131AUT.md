# R131AUT

## Descrição

Autorização Testes

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAut | Date | Não | Data da Autorização |
| SeqAut | Number(002,0) | Não | Sequência de autorização |
| CodHte | String(006) | Sim | Código da Habilidade Técnica autorizada |
| TipAva | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAva | Number(009,0) | Sim | Cadastro do Avaliador |
| SitTes | String(001) | Sim | Situação Atual do Teste |
| PerRec | String(001) | Sim | Define se o usuário pode recuperar o teste |
| TemPre | Number(005,0) | Sim | Tempo Previsto |
| HorIni | Number(005,0) | Sim | Hora de Início do Teste |
| HorTer | Number(005,0) | Sim | Hora de Término do Teste |
| DatFim | Date | Sim | Data de Término da Autorização |
| CodOem | Number(008,0) | Sim | Entidade responsável pela aplicação do teste |
| NumLot | Number(009,0) | Sim | Nr. do lote em que foi gerada a autorização |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAut
- SeqAut

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R131AUT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

