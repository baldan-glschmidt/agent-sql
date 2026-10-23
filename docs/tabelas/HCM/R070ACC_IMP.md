# R070ACC_IMP

## Descrição

Registro de Acesso - Importação Eventos Sistema Legado

---

## Resumo

- Campos: 30
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | Number(012,0) | Não | Número do Crachá |
| DatAcc | Date | Não | Data do Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| SeqAcc | Number(002,0) | Não | Sequência do Registro |
| TipAcc | Number(003,0) | Sim | Tipo do Acesso |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| CodFnc | Number(002,0) | Sim | Código da Função no Acesso |
| DirAcc | String(001) | Sim | Direção do Acesso |
| QtdAcc | Number(012,3) | Sim | Quantidade no Acesso |
| OriAcc | String(001) | Sim | Origem da Marcação |
| UsoMar | Number(002,0) | Sim | Uso da Marcação |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| DatApu | Date | Sim | Data de Apuração da Marcação |
| CodRef | Number(003,0) | Sim | Código da Refeição da Marcação |
| UsoRef | Number(001,0) | Sim | Uso da Refeição |
| ValRef | Number(012,3) | Sim | Valor da Refeição |
| CodSoR | Number(002,0) | Sim | Código da Solicitação no Relógio |
| FlaAcc | Number(001,0) | Sim | Flag do Acesso |
| CodBnf | Number(002,0) | Sim | Código do Benefício |
| StaRlg | Number(001,0) | Sim | Status do Coletor na Hora da Coleta |
| ExcPon | String(001) | Sim | Excluído do Ponto |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| MotIgn | Number(002,0) | Sim | Motivo Marcação Ignorada |
| CraAut | Number(012,0) | Sim | Número do crachá da pessoa autorizadora |
| NumNSR | Number(009,0) | Sim | Número NSR |
| GerAfd | String(001) | Sim | Gerado Arquivo AFD |
| Obs | String(050) | Sim | Observação |

---

## Chave Primária

- NumCra
- DatAcc
- HorAcc
- SeqAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
