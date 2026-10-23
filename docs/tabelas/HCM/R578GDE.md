# R578GDE

## Descrição

Avaliação de Competências - Gestão de Desempenho

---

## Resumo

- Campos: 19
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colaborador avaliado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador avaliado |
| NumCad | Number(009,0) | Não | Colaborador avaliado |
| CodCic | Number(003,0) | Não | Indica a qual Ciclo esta Avaliação pertence |
| NotCpt | Number(008,4) | Sim | Média da Avaliação por Competências |
| PerCpt | Number(007,4) | Sim | Percentual de atingimento da Avaliação por Competências |
| QuaCpt | Number(002,0) | Sim | Número do Quadrante referente a Avaliação por Competências |
| NotObj | Number(008,4) | Sim | Média da Avaliação de Objetivos |
| PerObj | Number(005,2) | Sim | Percentual de atingimento da Avaliação de Objetivos |
| QuaObj | Number(002,0) | Sim | Número do Quadrante referente a Avaliação de Objetivos |
| CodPer | Number(004,0) | Sim | Perfil do Formulário de Matriz de Gestão |
| SeqQua | Number(004,0) | Sim | Define o Quadrante calculado para o Avaliado |
| SeqQCF | Number(004,0) | Sim | Quadrante de Curva Forçada para o Avaliado |
| ObsQCF | String(8001) | Sim | Observação para Curva Forçada |
| SitGDE | Number(001,0) | Sim | Situação da Gestão de Desempenho |
| UsuGDE | Number(009,0) | Sim | Usuário que efetuou a última alteração |
| UltAtu | Number(014,6) | Sim | Data/Hora da última atualização na Gestão de Desempenho do colaborador |
| NotMGC | Number(008,4) | Sim | Média da Matriz de Gestão para Competências |
| NotMGO | Number(008,4) | Sim | Média da Matriz de Gestão para Objetivos |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578GDE_003

**Tabela:** R101CIC

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |

